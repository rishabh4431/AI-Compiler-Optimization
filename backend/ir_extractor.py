import subprocess

def generate_ir(input_file, output_file="temp.ll"):
    subprocess.run(f"clang -S -emit-llvm {input_file} -o {output_file}", shell=True)