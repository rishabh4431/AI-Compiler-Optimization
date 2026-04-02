import subprocess
import time

def run_with_opt(file, opt):
    exe = "temp.exe"

    subprocess.run(f"clang -{opt} {file} -o {exe}", shell=True)

    start = time.time()
    subprocess.run(exe, shell=True)
    end = time.time()

    return end - start