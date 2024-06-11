def verywrite(filename, modulename, input, output, gate):
    filename = "output.v"

    with open("./netlists/"+filename, "w") as file:
        file.write('modulename')
        file.write('module')
        file.write('input')
        file.write('output')
        file.write('endmodule')
    file.close()