from abc_cmd import *
import subprocess
import os
import re
import verilog_read
import sys
import random
import json
import verilog_write
import shutil
from tqdm import tqdm
import math
from utils import DummyPbar

from utils import count_gate, convert_to_wsl_path, get_cost, gate_list
from pick_singlegate import find_initial_mapping

# Function to recursively search for the string "and" in the JSON data

def map_annealing(netlist_path, cost_estimator_path, library_path, output_path, determine_dict = None, progress_bar = True):
    '''
    this function takes in the path to the netlist file, the path to the cost estimator, 
    the path to the library file, and the path to the output file.
    returns the final cost after doing simulated annealing algorithm.
    '''

    # read the verilog file
    modulename, inputs , outputs, wires, gates = verilog_read.read_verilog(netlist_path)
    with open(library_path, 'r') as file:
        data = json.load(file)  
    # count the number of each type of gate
    typesofgate = {gate: count_gate(data,gate) for gate in gate_list}
    #assign initial gate number to each gate
    gate_number_result = []
    
    if determine_dict:
        for gate in gates:
            gate_number_result.append(determine_dict[gate[0]])  
    else:
        for gate in gates:
            gate_number_result.append(random.randint(1,typesofgate[gate[0]]))  
    
    # get the initial state and initial cost
    tmpmapping_path = "tmp/tmpmapping.v"
    verilog_write.write_parsed_verilog(tmpmapping_path, modulename, inputs, outputs, gates, gate_number_result)
    current_cost = get_cost(cost_estimator_path, tmpmapping_path, library_path, "output/output.txt")

    initial_cost_stage_two = current_cost
    print("initial_cost_stage_two: ", initial_cost_stage_two)    
    
    # Simulated Annealing parameters
    initialTemperature = 1000.0
    Temperature = initialTemperature
    minTemperature = 0.001
    reduceRate = 0.99
    
    lengthOfGates = len(gates)
    #define costs
    neighbor_cost = 0
    final_cost = current_cost
    #create a copy of the initial mapping so that we can copy the best mapping to the output file
    shutil.copy(tmpmapping_path, output_path)
    
    #progress bar, may to not show
    if progress_bar:
        pbar = tqdm(total=math.ceil(math.fabs(math.log(Temperature/minTemperature)/math.log(reduceRate))))
    if not progress_bar:
        pbar = DummyPbar()
    
    while Temperature > minTemperature:
        # create a new gate number result
        new_gate_number_result = gate_number_result.copy()
        for i in range(0, min(math.floor(lengthOfGates * Temperature ), lengthOfGates * 10)):
            # move to neighbour state
            index = random.randint(0, lengthOfGates - 1)
            new_gate_number_result[index] = random.randint(1,typesofgate[gates[index][0]])
        # get the final_cost of the new state
        verilog_write.write_parsed_verilog(tmpmapping_path, modulename, inputs, outputs, gates, new_gate_number_result)
        neighbor_cost = get_cost(cost_estimator_path, tmpmapping_path, library_path, "output/output.txt")
        
        #compare the final_cost with the current_cost
        if neighbor_cost < current_cost:
            gate_number_result = new_gate_number_result
            current_cost = neighbor_cost
            if neighbor_cost < final_cost:
                final_cost = neighbor_cost
                shutil.copy(tmpmapping_path, output_path)
        else:
            if random.random() < pow(2.71828, (current_cost - neighbor_cost) / Temperature):
                # uphill move
                gate_number_result = new_gate_number_result
                current_cost = neighbor_cost
        #update the temperature
        Temperature = Temperature * reduceRate 
        pbar.update(1)
    pbar.close()
    
    final_cost_stage_two = final_cost
    print("Final Cost: ", final_cost_stage_two)    
    
    #redundant file deletion
    if os.path.isfile(tmpmapping_path):
        os.remove(tmpmapping_path)
    if os.path.isfile("output/output.txt"):
        os.remove("output/output.txt")
    
    return initial_cost_stage_two, final_cost_stage_two

def abc_annealing(netlist_path, cost_estimator_path, library_path, output_path, initial_dict = None, progress_bar = True):
    
    # Simulated Annealing parameters
    initialTemperature = 100.0
    Temperature = initialTemperature
    minTemperature = 0.1
    reduceRate = 0.8
    
    #define costs
    neighbor_cost = 0
    current_cost = float('inf')
    final_cost = current_cost
    
    #progress bar, may to not show
    if progress_bar:
        pbar = tqdm(total=math.ceil(math.fabs(math.log(Temperature/minTemperature)/math.log(reduceRate))))
    if not progress_bar:
        pbar = DummyPbar()

    folder = netlist_path[:netlist_path.rfind('/')+1]
    # out folder = "./tmp/"
    out_folder = "./tmp/"
    #filename = os.listdir(folder)[0]
    filename = netlist_path[netlist_path.rfind('/')+1:]
    # print("Filename: ", filename)
    gate_lib_path = "./data/lib/lib1.genlib"
    assert filename.endswith(".v")
    
    shutil.copy(netlist_path, "./tmp/"+ filename[:-2] + "_current.v")
    
    loopcount = 0
    while Temperature > minTemperature:
        loopcount += 1
        # print("\nLoop Count: ", loopcount,"\n")
        # get the initial state and initial cost
        
        cmd = get_random_cmd(out_folder, out_folder, gate_lib_path, filename[:-2] + "_current.v")
        # print("\nCommand = ", cmd, "\n")
        abc_exec(abc_path, cmd)
        # abc_print(abc_path, out_folder, filename[:-2] + "_current_abc.v")
        
        modulename, inputs , outputs, wires, gates = verilog_read.read_verilog(out_folder + filename[:-2] + "_current.v")
        
        if initial_dict is not None:
            gate_number_result = [initial_dict[gate[0]] for gate in gates]
        else:
            gate_number_result = [1 for gate in gates]
        
        verilog_write.write_parsed_verilog(out_folder + filename[:-2] + "_current_abc_parsed.v", modulename, inputs, outputs, gates, gate_number_result)
        
        neighbor_cost = get_cost(cost_estimator_path, out_folder + filename[:-2] + "_current_abc_parsed.v", library_path, "output/output.txt")
        if loopcount == 1:
            initial_cost_stage_one = neighbor_cost
            print ("initial_cost_stage_one: ", initial_cost_stage_one)
            
        if neighbor_cost < current_cost:
            verilog_write.write_verilog(out_folder + filename[:-2] + "_current.v", modulename, inputs, outputs, wires, gates)
            current_cost = neighbor_cost
        else:
            if random.random() < 0.05 * pow(2.71828, (current_cost - neighbor_cost) / Temperature):
                # uphill move
                verilog_write.write_verilog(out_folder + filename[:-2] + "_current.v", modulename, inputs, outputs, wires, gates)
                current_cost = neighbor_cost
        #update the temperature
        Temperature *= reduceRate 
        pbar.update(1)
    pbar.close()
    final_cost_stage_one = current_cost
    print("Stage 1 Cost: ", final_cost_stage_one)
    
    if os.path.isfile("output/output.txt"):
        os.remove("output/output.txt")
    if os.path.isfile(out_folder + filename[:-2] + "_current_abc.v"):
        os.remove(out_folder + filename[:-2] + "_current_abc.v")
    if os.path.isfile(out_folder + filename[:-2] + "_current_abc_parsed.v"):
        os.remove(out_folder + filename[:-2] + "_current_abc_parsed.v")
    
    return out_folder + filename[:-2] + "_current.v", initial_cost_stage_one, final_cost_stage_one

if __name__ == "__main__":
    '''
    example usage:
    type: python3 src/mappingannealing.py data/netlists/design1.v data/cost_estimators/cost_estimator_4 data/lib/lib1.json output/output.v
    '''
    
    # verilog_file_path = abc_annealing(netlist_path, cost_estimator_path, library_path, output_path)
    # map_annealing(verilog_file_path, cost_estimator_path, library_path, output_path)
    netlist_path = "data/netlists/design1.v"
    cost_estimator_path = "data/cost_estimators/cost_estimator_4"
    library_path = "data/lib/lib1.json"
    output_path = "output/output.v"
    
    module_name, _, _, _, _ = verilog_read.read_verilog(netlist_path)
    dictionary = find_initial_mapping(module_name, cost_estimator_path, library_path)
    verilog_file_path, initial_cost, stage_one_cost = abc_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar= True)
    map_annealing(verilog_file_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar = True)