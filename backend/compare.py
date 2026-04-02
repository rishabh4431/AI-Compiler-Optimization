import matplotlib.pyplot as plt

from backend.optimizer import run_with_opt

def compare(file):
    opts = ["O0", "O1", "O2", "O3"]
    times = []

    for opt in opts:
        t = run_with_opt(file, opt)
        times.append(t)

    return opts, times