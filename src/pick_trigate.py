# -------------------------------------------------------------------------------------------------
# Find the best assignment of each type of gates
# -------------------------------------------------------------------------------------------------
import subprocess
import re
import json
import os
import numpy as np
import verilog_write
from itertools import product
from tqdm import tqdm
from utils import is_single_gate, gate_list, number_of_choices, get_cost

def arrange_gates(level1, level2):
    '''
    Arrange the gates in the order of the number of inputs
    '''
    inputs, outputs, wires, gates = [], [], [], []
    gindex, pindex = 0, 1
    for gate in level1:
        if is_single_gate(gate):
            inputs.append(f"n{pindex}")
            wires.append(f"n{pindex}")
            gates.append( [gate, f"g{gindex}", f"n{pindex}", f"n{pindex + 1}"])
            pindex += 2
            gindex += 1
        else:
            inputs.append(f"n{pindex}")
            inputs.append(f"n{pindex + 1}")
            wires.append(f"n{pindex + 2}")
            gates.append( [gate, f"g{gindex}", f"n{pindex}", f"n{pindex + 1}", f"n{pindex + 2}"])
            pindex += 3
            gindex += 1
    for gate in level2:
        if is_single_gate(gate):
            outputs.append(f"n{pindex}")
            #wires.append(f"n{pindex}")
            gates.append( [gate, f"g{gindex}", wires[0], f"n{pindex}"])
            pindex += 1
            gindex += 1
        else:
            outputs.append(f"n{pindex}")
            #wires.append(f"n{pindex + 1}")
            gates.append( [gate, f"g{gindex}", wires[0], wires[1], f"n{pindex}"])
            pindex += 1
            gindex += 1
            
    return inputs, outputs, wires, gates


filename = "data/gate/tmp.v"
modulename = "module top_1598227639_809568180_776209382_1234615" 
cost_estimator_path = "data/cost_estimators/cost_estimator_1"
library_path = "data/lib/lib1.json"
tmp_output_path = "data/gate/output.txt"

best_gate =  {}
choices = number_of_choices(json.load(open(library_path)))
# order : this, in1, in2
for this_gate, in1_gate, in2_gate in tqdm(list(product(gate_list,repeat=3))):
    if is_single_gate(this_gate):
        best_gate[f"{this_gate}_{in1_gate}"] = [0] * choices[in1_gate]
        for type_1 in range(1,choices[in1_gate]+1):
            costs = []
            for type_this in range(1,choices[this_gate]+1):
                level1 = [f"{in1_gate}_{type_1}"]
                level2 = [f"{this_gate}_{type_this}"]
                inputs, outputs, wires, gates = arrange_gates(level1, level2)
                verilog_write.write_verilog(filename, modulename, inputs, outputs, wires, gates)
                cost = get_cost(cost_estimator_path, filename, library_path, tmp_output_path)
                costs.append(cost)
            best_number = costs.index(min(costs)) + 1
            best_gate[f"{this_gate}_{in1_gate}"][type_1-1] = best_number
    else:
        best_gate[f"{this_gate}_{in1_gate}_{in2_gate}"] = [ [0]* choices[in2_gate] for _ in range(choices[in1_gate])]
        for type1, type2 in product(range(1,choices[in1_gate]+1), range(1,choices[in2_gate]+1)):
            costs = []
            for type_this in range(1,choices[this_gate]+1):
                level1 = [f"{in1_gate}_{type1}",f"{in2_gate}_{type2}"]
                level2 = [f"{this_gate}_{type_this}"] 
                inputs, outputs, wires, gates = arrange_gates(level1, level2)
                verilog_write.write_verilog(filename, modulename, inputs, outputs, wires, gates)
                cost = get_cost(cost_estimator_path, filename, library_path, tmp_output_path)
                costs.append(cost)
            best_number = costs.index(min(costs)) + 1
            best_gate[f"{this_gate}_{in1_gate}_{in2_gate}"][type1-1][type2-1] = best_number

output_file_path = './data/gate/best_tri_gate.json'
with open(output_file_path, 'w') as json_file:
    json.dump(best_gate, json_file)
    
os.remove(filename)
os.remove(tmp_output_path)