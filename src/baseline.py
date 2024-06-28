from abc_cmd import *
import verilog_read
import verilog_write
import shutil
import csv
from utils import  get_cost


cost_arr = []
for i in range(1,7):
    for j in range(1,9):
        netlist = str(i)
        estimator = str(j)
        netlist_path = "data/netlists/design" + str(i) + ".v"
        cost_estimator_path = "data/cost_estimators/cost_estimator_" + str(j)
        library_path = "data/lib/lib1.json"
        output_path = "output/output.v"

        folder = netlist_path[:netlist_path.rfind('/')+1]

        out_folder = "./tmp/"
        filename = netlist_path[netlist_path.rfind('/')+1:]
        assert filename.endswith(".v")
        
        shutil.copy(netlist_path, "./tmp/"+ filename[:-2] + "_current.v")

        modulename, inputs , outputs, wires, gates = verilog_read.read_verilog(out_folder + filename[:-2] + "_current.v")

        gate_number_result = [1 for gate in gates]
        verilog_write.write_parsed_verilog(out_folder + filename[:-2] + "_current_abc_parsed.v", modulename, inputs, outputs, gates, gate_number_result)
        cost = get_cost(cost_estimator_path, out_folder + filename[:-2] + "_current_abc_parsed.v", library_path, "output/output.txt")
        print(f"baseline for netlist {i} and extimator {j} is {cost}")
        cost_arr.append(cost)
        with open('output/baseline.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(cost_arr)