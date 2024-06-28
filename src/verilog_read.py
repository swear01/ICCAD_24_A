import re
def read_verilog(filename):
    '''
    read verilog file (output, input, input)
    '''

    with open(filename, "r") as file:
        contents = file.read()
        
    contents = contents.split(";")
    lines = [line.strip().replace('\n','') for line in contents]
    # module name
    modulename = contents[0].split("\n")[0].strip().removesuffix("(")
    
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

def abc_read_verilog(filename):
    '''
    read verilog file (input, input, output)
    mainly for reading verilog file produced by abc
    '''

    with open(filename, "r") as file:
        contents = file.read()

    contents = contents.split(";")
    lines = [line.strip().replace('\n','') for line in contents]
    # module name
    modulename = contents[0].split("\n")[2].strip().removesuffix("(")
    
    
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
        if(line.startswith("\nendmodule")):
            break
        temp = []
        for i in line.replace("("," ").replace(")"," ").split(" "):
            if i.startswith(("A", "I", "O", "N", "B", "X","g","n","p")) :
                temp.append(i.lower())
        if (len(temp) == 5):
            temp = temp[0:2] + temp[4:5] + temp[2:4]

        if (len(temp) == 4):
            temp = temp[0:2] + temp[3:] + temp[2:3] + temp[2:3]
        gate.append(temp)


    return modulename, input, output, wire, gate

if __name__ == "__main__":
    read_verilog("./src/readtest.v")
    #abc_read_verilog("tmp/design1_abc.v")