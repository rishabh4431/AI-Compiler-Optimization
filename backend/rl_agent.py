import random
import pickle
import os

ACTIONS = ["O1", "O2", "O3"]

# 🔥 Base directory (AI_Compiler_Pro folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔥 Correct model path
MODEL_PATH = os.path.join(BASE_DIR, "model", "q_table.pkl")


class RLAgent:
    def __init__(self):
        self.q_table = {}

    def choose_action(self, state):
        # exploration (20%)
        if random.random() < 0.2:
            return random.choice(ACTIONS)

        # initialize state if not present
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in ACTIONS}

        # exploitation (best action)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward):
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in ACTIONS}

        self.q_table[state][action] += reward

    def save(self):
        # ensure model folder exists
        model_dir = os.path.join(BASE_DIR, "model")
        os.makedirs(model_dir, exist_ok=True)

        # save model
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(self.q_table, f)

    def load(self):
        # load model
        with open(MODEL_PATH, "rb") as f:
            self.q_table = pickle.load(f)