import abcc
import mappingannealing

# Logic synthesis with abc tool and simulated annealing
abc_path = "./src/abc"
gate_lib_path = "./data/lib/lib1.genlib"
folder = "./data/netlists/"
out_folder = "./tmp/"
filename = "design1.v"
assert filename.endswith(".v")
cmd = abcc.get_random_cmd(folder, out_folder, gate_lib_path, filename)
abcc.abc_exec(abc_path, cmd)
abcc.abc_print(abc_path, out_folder, filename[:-2] + "_abc.v")


# Technology mapping simulated annealing
#netlist_path = "tmp/design1_abc.v"
netlist_path = "data/netlists/design1.v"
library_path = "data/lib/lib1.json"
output_path = "output/output.v"
cost_estimator_path = "data/cost_estimators/cost_estimator_2"

dictionary = mappingannealing.initial_mapping_determine(netlist_path, cost_estimator_path, library_path)
mappingannealing.mapping_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary)
