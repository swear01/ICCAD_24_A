import json
import os
import sys
#include <tuple>

def read_gate(filename):
    # Read the gate file
    with open(filename, "r") as file:
        data = json.load(file)
    cell_num = int(data["information"]["cell_num"])
    attribute_num = int(data["information"]["attribute_num"])
    attributes = data["information"]["attributes"]
    # print(attributes)
    # print(attributes[0])
    # print("Cell number: ", cell_num)
    # print("Attribute number: ", attribute_num)
    gateList = [[data["cells"][i][attributes[j]] 
                for j in range(attribute_num)
                ]for i in range(cell_num)
                ]
    # Returns a list of lists, where each list is a gate
    # For example, gateList[0] is the first gate, and gateList[0][0] is the first attribute of the first gate  
    return gateList
    
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gateread.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    gateList = read_gate(filename)