import json
import csv
jsonfile = open("performance_record/rec.json",'r')
file = json.load(jsonfile)
# abc_cost_record = file["abc_cost_record"]
final_cost_record = file["final_cost_record"]
jsonfile.close()

output = []

for i in range(2,7):
    for j in range(1,9):
        output.append(final_cost_record[i-1][j-1][1])
with open('output/output1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(output)
print(final_cost_record)