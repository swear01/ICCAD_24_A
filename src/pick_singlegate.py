# -------------------------------------------------------------------------------------------------
# Find the best assignment of each type of gates
# -------------------------------------------------------------------------------------------------
import subprocess
import re
import json
import parsedverilog
from itertools import combinations_with_replacement

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
    if match:
        cost_value = float(match.group(1))
        return cost_value
    else:
        raise ValueError("Cost value not found in the output.")

dim1, dim2 = 6, 8

gate_cost = [[100  for _ in range(dim2)] for _ in range(dim1)]
best_gate = [100 for _ in range(dim1)]
target_gate = ["and", "or", "nand", "nor", "xor", "xnor"]
gate_types_num = [8, 8, 8, 8, 6, 6]

filename = "src/gate/b.v"
modulename = "module top_1598227639_809568180_776209382_1234615" 
inputs = ["n1" , "n2"]
outputs = ["n3"]
cost_estimator_path = "data/cost_estimators/cost_estimator_1"
tempmapping_path = "src/gate/b.v"
library_path = "data/lib/lib1.json"

for i in range(6):
    gates = [[target_gate[i], "g0", "n3", "n1", "n2"]]        
    temp = 100
    best_number = 0       
    for n in range(1,gate_types_num[i] + 1):
        gate_number_result = [n]
        parsedverilog.write_parsed_verilog(filename, modulename, inputs, outputs, gates ,gate_number_result)
        cost = getCost(cost_estimator_path, tempmapping_path, library_path, "output.txt")
        gate_cost[i][n-1] = cost
        if temp > cost:
            temp = cost
            best_number = n
            print(n)
    best_gate[i] = best_number

output_file_path = 'gate/gate_cost.json'
with open(output_file_path, 'w') as json_file:
    json.dump(gate_cost, json_file)
output_file_path = 'gate/best_gate.json'
with open(output_file_path, 'w') as json_file:
    json.dump(best_gate, json_file)