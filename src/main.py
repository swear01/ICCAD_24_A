import abc_cmd
import map_annealing
from verilog_read import abc_read_verilog, read_verilog
from verilog_write import write_verilog
import pick_singlegate

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

dictionary = map_annealing.initial_mapping_determine(netlist_path, cost_estimator_path, library_path)
map_annealing.map_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary)

read_verilog("tmp/design1_abc.v")
pick_singlegate.get_cost(cost_estimator_path, "tmp/design1_abc.v", library_path, output_path)