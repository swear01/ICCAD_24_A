import abcexe
import mappingannealing

# Logic synthesis with abc tool and simulated annealing
abc_path = "./src/abc"
gate_lib_path = "./data/lib/lib1.genlib"
folder = "./data/netlists/"
out_folder = "./tmp/"
filename = "design1.v"
assert filename.endswith(".v")
cmd = abcexe.get_random_cmd(folder, out_folder, gate_lib_path, filename)
abcexe.abc_exec(abc_path, cmd)
abcexe.abc_print(abc_path, out_folder, filename[:-2] + "_abc.v")


# Technology mapping simulated annealing
netlist_path = "tmp/design1_abc.v"
library_path = "data/lib/lib1.json"
output_path = "output/output.v"
cost_estimator_path = "data/cost_estimators/cost_estimator_2"

dictionary = mappingannealing.initial_mapping_determine(netlist_path, cost_estimator_path, library_path)
mappingannealing.abc_mapping_annealing_with_initial_determine(netlist_path, cost_estimator_path, library_path, output_path, dictionary)
