import subprocess
import re
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