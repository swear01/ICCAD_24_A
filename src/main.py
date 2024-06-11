import subprocess
import os
import re
import verilogread
import sys
import random
import json
import parsedverilog
import shutil

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
parsedverilog.write_parsed_verilog
cost_estimator_path = "data/cost_estimators/cost_estimator_1"
tempmapping_path = "src/gate/a.v"
library_path = "data/lib/lib1.json"
# cost_estimator_path = sys.argv[1]
# tempmapping_path = sys.argv[2]
# library_path = sys.argv[3]
print(getCost(cost_estimator_path, tempmapping_path, library_path, "output.txt"))