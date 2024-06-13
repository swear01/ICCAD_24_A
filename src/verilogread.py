# ---------------start---------------
# 2 functions: veryread, abc_veryread
# -----------------------------------
# veryread:
# read verilog file (output, input, input)
# ----------------------------------- 
# abc_veryread ()
# read verilog file (input, input, output)
# mainly for reading verilog file produced by abc
# ----------------end---------------
import re

def veryread(filename):

    with open(filename, "r") as file:
        contents = file.read()
        
    contents = contents.split(";")
    lines = [line.strip().replace('\n','') for line in contents]
    # module name
    modulename = contents[0].split("\n")[0] 
    
    # inputs
    inputs_data = lines[1].removeprefix("input").split(",")
    input = [i.strip() for i in inputs_data ]

    # outputs
    outputs_data = lines[2].removeprefix("output").split(",")
    output = [i.strip() for i in outputs_data]

    # wire
    wire_data = lines[3].removeprefix("wire").split(",")
    wire = [i.strip() for i in wire_data]

    #gates
    gate = []
    for line in lines[4:-1]:
        line = re.sub(r'[(),]', '', line)
        temp = line.split()
        if (len(temp) == 4):
            temp = temp[0:] + temp[3:]
            gate.append(temp)

    return modulename, input, output, wire, gate

def abc_veryread(filename):

    with open(filename, "r") as file:
        contents = file.read()

    lines = contents.split(";")
    # module name
    modulename = lines[0].split("\n")[2].split("(")[0]
    
    # inputs
    inputs_data = lines[1].replace(","," ").split(" ")
    input = [i for i in inputs_data if i.startswith(("n","p"))]

    # print(f"Input is {input}",)

    # outputs
    outputs_data = lines[2].replace(","," ").split(" ")
    output = [i for i in outputs_data if i.startswith(("n","p"))]
    # print(f"Output is {output}",)

    # wire
    wire_data = lines[3].replace(","," ").split(" ")
    wire = [i for i in wire_data if i.startswith(("n","p"))]
    # print(f"Wire is {wire}")

    #gates
    gate = []

    loc = 4
    while True:
        if(lines[loc].startswith("\nendmodule")):
            break
        temp = []
        for i in lines[loc].replace("("," ").replace(")"," ").split(" "):
            if i.startswith(("A", "I", "O", "N", "B", "X")) :
                temp.append(i.lower())
            if (i.startswith(("g","n","p"))):
                temp.append(i)

        if (len(temp) == 5):
            temp = temp[0:2] + temp[4:5] + temp[2:4]
            gate.append(temp)
        if (len(temp) == 4):
            temp = temp[0:2] + temp[3:] + temp[2:3] + temp[2:3]
            gate.append(temp)

        loc += 1
    # print(modulename)
    # print(input)
    # print(output)
    # print(wire)
    # print(gate)
    # print(f"gate is {gate}")
    return modulename, input, output, wire, gate

if __name__ == "__main__":
    veryread("./src/readtest.v")
    #abc_veryread("tmp/design1_abc.v")