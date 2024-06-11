def veryread(filename):

    with open(filename, "r") as file:
        contents = file.read()

    lines = contents.split(";")
    # module name
    modulename = lines[0].split("\n")[0]
    
    # inputs
    inputs_data = lines[1].split("n")
    input = []
    for i in inputs_data:
        if (i.startswith("0") or 
            i.startswith("1") or 
            i.startswith("2") or 
            i.startswith("3") or 
            i.startswith("4") or 
            i.startswith("5") or 
            i.startswith("6") or
            i.startswith("7") or 
            i.startswith("8") or 
            i.startswith("9") ):
            input.append(int(i.split(" ")[0]))
    # print(f"Input is {input}",)

    # outputs
    outputs_data = lines[2].split("n")
    output = []
    for i in outputs_data:
        if (i.startswith("0") or 
            i.startswith("1") or 
            i.startswith("2") or 
            i.startswith("3") or 
            i.startswith("4") or 
            i.startswith("5") or 
            i.startswith("6") or
            i.startswith("7") or 
            i.startswith("8") or 
            i.startswith("9") ):
            output.append(int(i.split(" ")[0]))
    # print(f"Output is {output}",)

    # wire
    wire_data = lines[3].split("n")
    wire = []
    for i in wire_data:
        if (i.startswith("0") or 
            i.startswith("1") or 
            i.startswith("2") or 
            i.startswith("3") or 
            i.startswith("4") or 
            i.startswith("5") or 
            i.startswith("6") or
            i.startswith("7") or 
            i.startswith("8") or 
            i.startswith("9") ):
            wire.append(int(i.split(" ")[0]))
    # print(f"Wire is {wire}")

    #gates
    gate = []

    loc = 4
    while True:
        if(lines[loc].startswith("\nendmodule")):
            break
        temp = []
        for i in lines[loc].split(" "):
            if (
            i.startswith("a") or 
            i.startswith("o") or
            i.startswith("g") or 
            i.startswith("n") or 
            i.startswith("b") or 
            i.startswith("x")):
                temp.append(i)

        if (len(temp) == 5):
            gate.append(temp)
        if (len(temp) == 4):
            temp = temp[0:] + temp[3:]
            gate.append(temp)

        loc += 1

    # print(f"gate is {gate}")
    return modulename, input, output, wire, gate

if __name__ == "__main__":
    veryread("./ICCAD_24_A/src/readtest.v")