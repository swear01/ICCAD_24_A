import subprocess
import os
import re
import verilogread
import sys
import random
import json
import parsedverilog
import shutil

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

def getCost(cost_estimator_path, netlist_path, library_path, output_path):
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

def mappingAnnealing(netlist_path, cost_estimator_path, library_path, output_path):
    # read the verilog file
    inputs , outputs, wires, gates = verilogread.veryread(netlist_path)
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
    tempmapping_path = "tempmapping.v"
    parsedverilog.writeParsedVerilog(tempmapping_path, inputs, outputs, gates, gate_number_result)
    current_cost = getCost(cost_estimator_path, tempmapping_path, library_path, "output.txt")
    print("Initial Cost: ", current_cost)
    
    # Temperature = 10 * len(gates)
    Temperature = 20
    lengthOfGates = len(gates)
    neighbor_cost = 0
    final_cost = current_cost
    shutil.copy(tempmapping_path, output_path)
    
    while Temperature > 1:
        for i in range(0, lengthOfGates):
            # create a new gate number result
            new_gate_number_result = gate_number_result.copy()
            # move to neighbour state
            new_gate_number_result[i] = random.randint(1,typesofgate[gates[i][0]])
            # get the final_cost of the new state
            parsedverilog.writeParsedVerilog(tempmapping_path, inputs, outputs, gates, new_gate_number_result)
            neighbor_cost = getCost(cost_estimator_path, tempmapping_path, library_path, "output.txt")
            
            #compare the final_cost with the current_cost
            if neighbor_cost < current_cost:
                gate_number_result = new_gate_number_result
                current_cost = neighbor_cost
                if neighbor_cost < final_cost:
                    final_cost = neighbor_cost
                    shutil.copy("parsedgate.v", sys.argv[4])
            else:
                if random.random() < pow(2.71828, (current_cost - neighbor_cost) / Temperature):
                    # uphill move
                    gate_number_result = new_gate_number_result
                    current_cost = neighbor_cost
        #update the temperature
        Temperature = Temperature - 1 
    print("Final Cost: ", final_cost)
    
    if os.path.isfile(tempmapping_path):
        os.remove(tempmapping_path)
    if os.path.isfile("output.txt"):
        os.remove("output.txt")
    
    return final_cost

if __name__ == "__main__":
    if(len(sys.argv) != 5):
        print("Usage: python3 getinitialgatenumber.py <verilog_file> <cost_estimator> <library> <output.v>")
        sys.exit(1)
    
    mappingAnnealing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])