# -------------------------------------------------------------------------------------------------
# Try to determine the assignment of the gate given the previous 2 gates' types and assignments
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
dim1, dim2, dim3, dim4, dim5, dim6 = 6, 6, 6, 8, 8, 8
map_rule = [[[[[100 for _ in range(dim5)] for _ in range(dim4)] for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
map_data = [[[[[[100 for _ in range(dim6)] for _ in range(dim5)] for _ in range(dim4)] for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
target_gate = ["and", "or", "nand", "nor", "xor", "xnor"]
gate_types_num = [8, 8, 8, 8, 6, 6]

filename = "src/gate/b.v"
modulename = "module top_1598227639_809568180_776209382_1234615" 
inputs = ["n1" , "n2" , "n4" , "n5"]
outputs = ["n7"]
cost_estimator_path = "data/cost_estimators/cost_estimator_7"
tempmapping_path = "src/gate/b.v"
library_path = "data/lib/lib1.json"

for i, j in combinations_with_replacement(range(6),2):
    for k in range(6):
        print(i,j,k)
        gates = [[target_gate[i], "g0", "n3", "n1", "n2"],
                [target_gate[j], "g1", "n6", "n4", "n5"],
                [target_gate[k], "g2", "n7", "n3", "n6"]]        
        for l in range(1, gate_types_num[i] + 1):
            for m in range(1, gate_types_num[j] + 1):
                best_cost = 100
                best_number = 0                
                for n in range(1,gate_types_num[k] + 1):
                    gate_number_result = [l, m, n]
                    parsedverilog.write_parsed_verilog(filename, modulename, inputs, outputs, gates ,gate_number_result)
                    cost = getCost(cost_estimator_path, tempmapping_path, library_path, "output.txt")
                    print(cost)
                    map_data[i][j][k][l-1][m-1][n-1] = cost
                    if best_cost > cost:
                        best_cost = cost
                        best_number = n
                map_rule[i][j][k][l-1][m-1] = best_number

output_file_path = 'gate/map_rule.json'
with open(output_file_path, 'w') as json_file:
    json.dump(map_rule, json_file)
output_file_path = 'gate/map_data.json'
with open(output_file_path, 'w') as json_file:
    json.dump(map_data, json_file)