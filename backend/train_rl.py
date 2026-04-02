import os
from backend.rl_agent import RLAgent
from backend.optimizer import run_with_opt
from backend.ir_extractor import generate_ir
from backend.feature_extractor import extract_ir_features

agent = RLAgent()

for file in os.listdir("samples"):
    path = "samples/" + file

    generate_ir(path)
    features = extract_ir_features("temp.ll")

    state = tuple(features.values())

    for opt in ["O1", "O2", "O3"]:
        time_taken = run_with_opt(path, opt)

        reward = -time_taken
        agent.update(state, opt, reward)

agent.save()
print("Training Complete!")