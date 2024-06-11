import subprocess
import os
import re
import verilogread
import sys
import random
import json
import parsedverilog
import shutil
from tqdm import tqdm
import math

# Function to recursively search for the string "and" in the JSON data
def count_gate(data, typeofgate):
    count = 0
    for cell in data['cells']:
        # Check if the cell_type is 'and'
        if cell['cell_type'] == typeofgate:
            count += 1
    return count

def convert_to_wsl_path(path):
    drive, path = os.path.splitdrive(path)
    path = path.replace('\\', '/')
    return f'/mnt/{drive[0].lower()}{path}'

def get_cost(cost_estimator_path, netlist_path, library_path, output_path):
    # Construct the WSL command
    command = [
        # 'wsl',  # Use WSL to run the command
        cost_estimator_path,
        '-netlist', netlist_path,
        '-library', library_path,
        '-output', output_path
    ]
    # print (command)
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check for errors
    match = re.search(r'cost\s*=\s*([0-9.]+)', result.stdout)
    if match:
        cost_value = float(match.group(1))
        return cost_value
    else:
        raise ValueError("Cost value not found in the output.")

def mapping_annealing(netlist_path, cost_estimator_path, library_path, output_path):
    # read the verilog file
    modulename, inputs , outputs, wires, gates = verilogread.veryread(netlist_path)
    with open(library_path, 'r') as file:
        data = json.load(file)  
    # count the number of each type of gate
    typesofgate = {'and': count_gate(data,'and'), 'or' : count_gate(data,'or'),
                'xor' : count_gate(data,'xor'), 'nand' : count_gate(data,'nand'),
                'nor' : count_gate(data,'nor'), 'xnor' : count_gate(data,'xnor'),
                'not' : count_gate(data,'not'), 'buf' : count_gate(data,'buf')}
    gate_number_result = []
    for gate in gates:
        gate_number_result.append(random.randint(1,typesofgate[gate[0]]))  
    
    # get the initial state and initial cost
    tempmapping_path = "temp/tempmapping.v"
    parsedverilog.write_parsed_verilog(tempmapping_path, modulename, inputs, outputs, gates, gate_number_result)
    current_cost = get_cost(cost_estimator_path, tempmapping_path, library_path, "output/output.txt")
    print("Initial Cost: ", current_cost)
    
    # Temperature = 10 * len(gates)
    initialTemperature = 1000.0
    Temperature = initialTemperature
    minTemperature = 0.001
    reduceRate = 0.99
    
    lengthOfGates = len(gates)
    neighbor_cost = 0
    final_cost = current_cost
    shutil.copy(tempmapping_path, output_path)
    pbar = tqdm(total=math.ceil(math.fabs(math.log(Temperature/minTemperature)/math.log(reduceRate))))
    while Temperature > minTemperature:
        # create a new gate number result
        new_gate_number_result = gate_number_result.copy()
        for i in range(0, min(math.floor(lengthOfGates * Temperature ), lengthOfGates * 10)):
            # move to neighbour state
            index = random.randint(0, lengthOfGates - 1)
            new_gate_number_result[index] = random.randint(1,typesofgate[gates[index][0]])
        # get the final_cost of the new state
        parsedverilog.write_parsed_verilog(tempmapping_path, modulename, inputs, outputs, gates, new_gate_number_result)
        neighbor_cost = get_cost(cost_estimator_path, tempmapping_path, library_path, "output/output.txt")
        
        #compare the final_cost with the current_cost
        if neighbor_cost < current_cost:
            gate_number_result = new_gate_number_result
            current_cost = neighbor_cost
            if neighbor_cost < final_cost:
                final_cost = neighbor_cost
                shutil.copy(tempmapping_path, sys.argv[4])
        else:
            if random.random() < pow(2.71828, (current_cost - neighbor_cost) / Temperature):
                # uphill move
                gate_number_result = new_gate_number_result
                current_cost = neighbor_cost
        #update the temperature
        Temperature = Temperature * reduceRate 
        pbar.update(1)
    pbar.close()
    print("Final Cost: ", final_cost)
    
    if os.path.isfile(tempmapping_path):
        os.remove(tempmapping_path)
    if os.path.isfile("output/output.txt"):
        os.remove("output/output.txt")
    
    return final_cost

def initial_mapping(netlist_path, cost_estimator_path, library_path):
    # read the verilog file
    modulename, inputs , outputs, wires, gates = verilogread.veryread(netlist_path)
    with open(library_path, 'r') as file:
        data = json.load(file)  
    # count the number of each type of gate
    typesofgate = {'and': count_gate(data,'and'), 'or' : count_gate(data,'or'),
                'xor' : count_gate(data,'xor'), 'nand' : count_gate(data,'nand'),
                'nor' : count_gate(data,'nor'), 'xnor' : count_gate(data,'xnor'),
                'not' : count_gate(data,'not'), 'buf' : count_gate(data,'buf')}
    gate_number_result = []
    for gate in gates:
        gate_number_result.append(1)  
    
    # get the initial state and initial cost
    tempmapping_path = "temp/initialtempmapping.v"
    parsedverilog.write_parsed_verilog(tempmapping_path, modulename, inputs, outputs, gates, gate_number_result)
    current_cost = get_cost(cost_estimator_path, tempmapping_path, library_path, "output/output.txt")
    print("Initial Cost: ", current_cost)
    
    initialDictionary = typesofgate.copy()
    lengthOfGates = len(gates)
    neighbor_cost = current_cost
    # shutil.copy(tempmapping_path, output_path)
    
    for key in typesofgate.keys():
        for num in range(1, typesofgate[key]+1):
            for i in range(0, lengthOfGates):
                # create a new gate number result
                new_gate_number_result = gate_number_result.copy()
                # move to neighbour state
                if(gates[i][0] == key):
                    new_gate_number_result[i] = num
            # get the final_cost of the new state
            parsedverilog.write_parsed_verilog(tempmapping_path, inputs, outputs, gates, new_gate_number_result)
            neighbor_cost = get_cost(cost_estimator_path, tempmapping_path, library_path, "output/output.txt")
            
            #compare the final_cost with the current_cost
            if neighbor_cost < current_cost:
                gate_number_result = new_gate_number_result
                current_cost = neighbor_cost
                initialDictionary[key] = num
                
    print("Final Cost: ", neighbor_cost)
    
    if os.path.isfile(tempmapping_path):
        os.remove(tempmapping_path)
    if os.path.isfile("output/output.txt"):
        os.remove("output/output.txt")
    
    return initialDictionary

if __name__ == "__main__":
    if(len(sys.argv) != 5):
        print("Usage: python3 getinitialgatenumber.py <verilog_file> <cost_estimator> <library> <output.v>")
        sys.exit(1)
    
    mapping_annealing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # initialDict = initialMapping(sys.argv[1], sys.argv[2], sys.argv[3])
    # print(initialDict)