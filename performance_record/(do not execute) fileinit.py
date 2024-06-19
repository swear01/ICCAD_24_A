import shutil
for i in range(1,7):
    for j in range(1,9):
        shutil.copy("performance_record/bench.json",f"performance_record/{str(i)}-{str(j)}/{str(i)}-{str(j)}_hty.json")

