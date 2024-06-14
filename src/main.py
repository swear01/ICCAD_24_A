import abc_cmd
import map_annealing

from verilog_read import abc_read_verilog, read_verilog
from verilog_write import write_verilog
import pick_singlegate
import verilog_read
import pick_singlegate

# greedy
    
#
for i in range(1,7):
    for j in range(1,9):
        print(i,j)
        s1 = "data/netlists/design" + str(i) + ".v"
        s2 = "data/cost_estimators/cost_estimator_" + str(j)
        s3 = "data/lib/lib1.json"
        s4 = "output/output.v"
        # verilog_file_path = abc_annealing(s1, s2, s3, s4)
        # mapping_annealing(verilog_file_path, s2, s3, s4)

        dictionary = map_annealing.initial_mapping_determine(s1, s2, s3)
        verilog_file_path = map_annealing.abc_annealing(s1, s2, s3, s4, dictionary)
        map_annealing.mapping_annealing(verilog_file_path, s2, s3, s4, dictionary)

'''
# Logic synthesis with abc tool and simulated annealing
abc_path = "./src/abc"
gate_lib_path = "./data/lib/lib1.genlib"
folder = "./data/netlists/"
out_folder = "./tmp/"
filename = "design1.v"
assert filename.endswith(".v")
cmd = abc_cmd.get_random_cmd(folder, out_folder, gate_lib_path, filename)
abc_cmd.abc_exec(abc_path, cmd)
write_verilog(out_folder + filename[:-2] + "_abc.v" ,*abc_read_verilog(out_folder + filename[:-2] + "_abc.v"))
abc_cmd.abc_print(abc_path, out_folder, filename[:-2] + "_abc.v")


# Technology mapping simulated annealing
#netlist_path = "tmp/design1_abc.v"
netlist_path = "data/netlists/design1.v"
library_path = "data/lib/lib1.json"
output_path = "output/output.v"
cost_estimator_path = "data/cost_estimators/cost_estimator_2"


# dictionary = mappingannealing.initial_mapping_determine(netlist_path, cost_estimator_path, library_path)
# mappingannealing.mapping_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary)

verilog_read.abc_read_verilog("tmp/design1_abc.v")
pick_singlegate.get_cost(cost_estimator_path, netlist_path, library_path, output_path)
'''
