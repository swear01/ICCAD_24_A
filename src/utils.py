gate_list: list[str] = ["and", "or", "nand", "nor", "xor", "xnor", "not", "buf"]

def is_single_gate(gate:str) -> bool:
    '''
    check if the gate is a single gate
    '''
    if gate.startswith(("not", "buf")):
        return True
    return False

def number_of_choices(libs: dict) -> dict[str, int]:
    '''
    return the number of choices for each type of gates
    '''
    libs = libs["cells"]
    result = {gate: 0 for gate in gate_list}
    for cell in libs:
        result[cell["cell_type"]] += 1
    return result