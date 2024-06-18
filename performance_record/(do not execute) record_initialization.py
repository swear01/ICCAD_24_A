# Run this file to clear all record data
import json
dim1, dim2 = 6, 8
dim3 = 2
abc_cost_record = [[[1E15 for _ in range(dim3)]  for _ in range(dim2)] for _ in range(dim1)]
final_cost_record = [[[1E15 for _ in range(dim3)]  for _ in range(dim2)] for _ in range(dim1)]

data = {
    "abc_cost_record": abc_cost_record,
    "final_cost_record": final_cost_record
}

with open("rec.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)