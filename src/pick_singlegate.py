# -------------------------------------------------------------------------------------------------
# Find the best assignment of each type of gates
# -------------------------------------------------------------------------------------------------
import subprocess
import re
import json
import os
from . import verilog_write
from .utils import is_single_gate, gate_list, number_of_choices, get_cost

filename = "tmp/tmp.v"
modulename = "module top_1598227639_809568180_776209382_1234615" 
cost_estimator_path = "data/cost_estimators/cost_estimator_1"
library_path = "data/lib/lib1.json"
tmp_output_path = "data/gate/output.txt"
output_file_path = './data/gate/best_single_gate.json'

def find_initial_mapping(modulename, cost_estimator_path, library_path,):
    best_gate =  {}
    choices = number_of_choices(json.load(open(library_path)))
    for gate in gate_list:
        costs = []
        if is_single_gate(gate):
            inputs, outputs = ["n1"], ["n3"]
            gates = [[f"{gate}_{i}", "g0", "n1", "n3"] for i in range(1, choices[gate] + 1)]
        else:
            inputs, outputs = ["n1" , "n2"], ["n3"]
            gates = [[f"{gate}_{i}", "g0", "n1", "n2", "n3"] for i in range(1, choices[gate] + 1)]
                        
        for gate_i in gates:
            verilog_write.write_verilog(filename, modulename, inputs, outputs, [], [gate_i])
            cost = get_cost(cost_estimator_path, filename, library_path, tmp_output_path)
            costs.append(cost)
        best_number = costs.index(min(costs)) + 1
        best_gate[gate] = best_number


    with open(output_file_path, 'w') as json_file:
        json.dump(best_gate, json_file)
        
    os.remove(filename)
    os.remove(tmp_output_path)
    
    return best_gate