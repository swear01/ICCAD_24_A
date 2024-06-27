from src.verilog_read import abc_read_verilog, read_verilog
from src.verilog_write import write_verilog
from src import verilog_read, map_annealing
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("-cost_function", type = str, help = "The path to the cost function", default="data/cost_estimators/cost_estimator_4")
argparser.add_argument("-netlist", type = str, help = "The path to the netlist", default="data/netlists/design1.v")
argparser.add_argument("-library", type = str, help = "The path to the library", default="data/lib/lib1.json")
argparser.add_argument("-output", type = str, help = "The path to the output", default="output/output.v")

args = argparser.parse_args()

netlist_path = args.netlist
cost_estimator_path = args.cost_function
library_path = args.library
output_path = args.output
initial_temperature = 0.01

module_name, _, _, _, _ = verilog_read.read_verilog(netlist_path)
dictionary = map_annealing.find_initial_mapping(module_name, cost_estimator_path, library_path)

verilog_file_path, initial_cost_stage_one, final_cost_stage_one  = map_annealing.abc_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar= True)

initial_cost_stage_two, final_cost_stage_two = map_annealing.map_annealing(verilog_file_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar = True, initial_temperature = initial_temperature)




