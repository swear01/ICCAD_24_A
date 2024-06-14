# -------------------------------------------------------------------------------------------------
# Find the best assignment of each type of gates
# -------------------------------------------------------------------------------------------------
import subprocess
import re
import json
import os
import parsedverilog
from utils import is_single_gate, gate_list, number_of_choices

def getCost(cost_estimator_path, netlist_path, library_path, output_path):
    # Construct the WSL command
    command = [
        # 'wsl',  # Use WSL to run the command
        cost_estimator_path,
        '-netlist', netlist_path,
        '-library', library_path,
        '-output', output_path
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check for errors
    match = re.search(r'cost\s*=\s*([0-9.]+)', result.stdout)
    if not match:
        raise ValueError("Cost value not found in the output.")
    cost_value = float(match.group(1))
    return cost_value
        

filename = "data/gate/tmp.v"
modulename = "module top_1598227639_809568180_776209382_1234615" 
cost_estimator_path = "data/cost_estimators/cost_estimator_1"
library_path = "data/lib/lib1.json"
tmp_output_path = "data/gate/output.txt"


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
        parsedverilog.write_verilog(filename, modulename, inputs, outputs, [], [gate_i])
        cost = getCost(cost_estimator_path, filename, library_path, tmp_output_path)
        costs.append(cost)
    best_number = costs.index(min(costs)) + 1
    best_gate[gate] = best_number

output_file_path = './data/gate/best_single_gate.json'
with open(output_file_path, 'w') as json_file:
    json.dump(best_gate, json_file)
    
os.remove(filename)
os.remove(tmp_output_path)