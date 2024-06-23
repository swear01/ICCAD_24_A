import abc_cmd
import map_annealing
import shutil
from verilog_read import abc_read_verilog, read_verilog
from verilog_write import write_verilog
import pick_singlegate
import verilog_read
import pick_singlegate
import json

jsonfile = open("performance_record/rec.json",'r')
file = json.load(jsonfile)
abc_cost_record = file["abc_cost_record"]
final_cost_record = file["final_cost_record"]
jsonfile.close()

for times in range(10):
    for i in range(1,2):
        for j in range(2,3):
            netlist = str(i)
            estimator = str(j)
            netlist_path = "data/netlists/design" + str(i) + ".v"
            cost_estimator_path = "data/cost_estimators/cost_estimator_" + str(j)
            library_path = "data/lib/lib1.json"
            output_path = "output/output.v"
            initial_temperature_2 = 1000000000.0


            # get benchmark and history
            history_file = f"performance_record/{netlist}-{estimator}/{netlist}-{estimator}_hty.json"
            history_json = open(history_file,'r')
            history_data = json.load(history_json)
            benchmark = history_data["benchmark"]
            history = history_data["history"]
            history_json.close()
            
            stage_one_best = False
            stage_two_best = False
            
            
            module_name, _, _, _, _ = verilog_read.read_verilog(netlist_path)
            dictionary = map_annealing.find_initial_mapping(module_name, cost_estimator_path, library_path)
            
            verilog_file_path, initial_cost_stage_one, final_cost_stage_one  = map_annealing.abc_annealing(netlist_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar= True)
            
            shutil.copy(verilog_file_path, f"performance_record/{str(i)}-{str(j)}/{str(i)}-{str(j)}_stage_one_result-{str(benchmark)}")
            
            initial_cost_stage_two, final_cost_stage_two = map_annealing.map_annealing(verilog_file_path, cost_estimator_path, library_path, output_path, dictionary, progress_bar = True, initial_temperature = initial_temperature_2)

            shutil.copy(output_path, f"performance_record/{str(i)}-{str(j)}/{str(i)}-{str(j)}_stage_two_result-{str(benchmark)}")

            if final_cost_stage_one < abc_cost_record[i-1][j-1][0]:
                abc_cost_record[i-1][j-1] = [final_cost_stage_one, final_cost_stage_two]
                stage_one_best = True
            
            if final_cost_stage_two < final_cost_record[i-1][j-1][1]:
                final_cost_record[i-1][j-1] = [final_cost_stage_one, final_cost_stage_two]
                stage_two_best = True
            
            benchmark += 1
            history.append([[final_cost_stage_one, final_cost_stage_two, benchmark,
                            "SA1type", 100, "SA2type", initial_temperature_2, stage_one_best, stage_two_best]])
            
            new_history = {
            "benchmark": benchmark,
            "history": history
            }
            
            with open(history_file, 'w') as json_file:
                json.dump(new_history, json_file, indent = 4)
            json_file.close()        
            
            
            data = {
                "abc_cost_record": abc_cost_record,
                "final_cost_record": final_cost_record
            }
            
            # print(data)
            with open("performance_record/rec.json", 'w') as json_file:
                json.dump(data, json_file, indent = 4)
            json_file.close()
        





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
