# Interface For Batch Mode ABC
# type: ignore

import subprocess
import os 
import random
from verilog_read import abc_read_verilog
from verilog_write import write_verilog

# possible_cmds = [
# "strash; balance;",
# "strash; rewrite -l;",
# "strash; rewrite -lz;",
# "strash; dsd; strash;",
# "strash; iresyn -l;",
# "strash; dc2 -bl;",
# "strash; refactor -N 15 -lz;",
# "strash; orchestrate;",
# "strash; resub -lz;",
# "strash; csweep; trim;",
# # "&get; &muxdec; &put;",
# ]

possible_cmds = [
"src_rw      ;",
"src_rs      ;",
"src_rws     ;",
"resyn2rs    ;",
"r2rs        ;",
"compress2rs ;",
"c2rs        ;",
"resyn2rs   ;",
"compress2rs;",
"resyn       ;",
"resyn2      ;",
"resyn2a     ;",
"resyn3      ;",
"compress    ;",
"compress2   ;",
"choice      ;",
"choice2     ;",
"rwsat       ;",
"drwsat2     ;",
"share       ;",
# "addinit     ;",
"blif2aig    ;",
# "v2p         ;",
# "g2p         ;",
# "&sw_        ;",
# "&fx_        ;",
# "&dc3        ;",
# "&dc4        ;",
"rec_start3; recadd3     ;",
]
abc_path = "./src/abc"
gate_lib_path = "./data/lib/lib1.genlib"

def get_random_cmd(in_folder, out_folder, gate_lib, filename) -> str:
    choosen = random.choice(possible_cmds)
    prefix = f"read_verilog {in_folder}{filename};strash;"
    suffix = f"read_library {gate_lib};map;write_verilog {out_folder}{filename[:-2]}_abc.v;"
    return prefix + choosen + suffix

def abc_exec(abc_path, cmd):
    subprocess.run([abc_path, "-c", cmd])
    
def abc_print(abc_path, folder, filename):
    abc_exec(abc_path,f"read_verilog {folder}{filename}; print_stats;")

if __name__ == "__main__":
    folder = "./data/netlists/"
    #folder = "./tmp/"
    out_folder = "./tmp/"
    #filename = os.listdir(folder)[0]
    filename = "design1.v"
    gate_lib_path = "./data/lib/lib1.genlib"
    assert filename.endswith(".v")
    cmd = get_random_cmd(folder, out_folder, gate_lib_path, filename)
    print(cmd)
    abc_exec(abc_path, cmd)
    write_verilog(out_folder + filename[:-2] + "_abc.v" ,*abc_read_verilog(out_folder + filename[:-2] + "_abc.v"))
    
    abc_print(abc_path, out_folder, filename[:-2] + "_abc.v")
    
    
    

 