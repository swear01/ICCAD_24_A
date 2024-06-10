def writeParsedVerilog(filename, inputs, outputs, gates ,gate_number_result):
    with open(filename, "w") as file:
        inputlist = ", ".join(f"n{input}" for input in inputs)
        outputlist = ", ".join(f"n{output}" for output in outputs)
        file.write('module top_1598227639_809568180_776209382_1234615 ' + "(" + inputlist + ", " + outputlist + ");\n")
        file.write("  input " + inputlist + ';' + '\n')
        file.write("  output " + outputlist + ';' + '\n')
        for i in range(0, len(gates)):
            if gates[i][3] != gates[i][4]:
                file.write("  " + gates[i][0] + "_" + str(gate_number_result[i]) +" "+ gates[i][1] + "(" + gates[i][3] + "," + gates[i][4] + "," + gates[i][2] + ");\n")
            else:
                file.write("  " + gates[i][0] + "_" + str(gate_number_result[i]) +" "+ gates[i][1] + "(" + gates[i][4] + "," + gates[i][2] + ");\n")
        file.write('endmodule\n')