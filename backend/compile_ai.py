from backend.ir_extractor import generate_ir
from backend.feature_extractor import extract_ir_features
from backend.dl_model import predict, train
from backend.compare import compare
import subprocess
import time

OPT_MAP = ["O0", "O1", "O2", "O3"]

def compile_ai(file):
    generate_ir(file)
    features = extract_ir_features("temp.ll")

    # 🔥 DL prediction
    pred_index = predict(features)
    opt = OPT_MAP[pred_index]

    print(f"[AI-DL] Selected Optimization: -{opt}")

    subprocess.run(f"clang -{opt} {file} -o output.exe", shell=True)

    start = time.time()
    subprocess.run("output.exe", shell=True)
    end = time.time()

    exec_time = end - start
    print(f"Execution Time: {exec_time:.5f} sec")

    # 🔥 continuous learning
    train(features, pred_index)

    return opt, exec_time