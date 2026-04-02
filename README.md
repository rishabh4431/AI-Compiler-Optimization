AI-Assisted Compiler Optimization (Deep Learning Based)

## Overview
This project presents an intelligent compiler optimization system that uses **Deep Learning** to automatically select the best optimization level (O0–O3) for a given C program.

Unlike traditional compilers that use fixed heuristics, this system **learns from program behavior** and improves over time using continuous learning.

##  Key Features

1.LLVM IR Feature Extraction  
2. Deep Learning Model (Neural Network)  
3. Continuous Learning (Adaptive System)  
4. Automatic Optimization Selection (O0–O3)  
5. Performance Comparison Graph  
6. Interactive Streamlit Dashboard  

##  How It Works

C Code -> LLVM IR -> Feature Extraction -> Deep Learning Model -> Optimization Selection -> Execution -> Performance Analysis

##  Tech Stack

1 -  Python  
2 -  TensorFlow / Keras  
3 -  LLVM / Clang  
4 -  Matplotlib  
5 -  Streamlit  

##  Project Structure
AI_Compiler_Pro/
│
├── backend/
│ ├── ir_extractor.py
│ ├── feature_extractor.py
│ ├── dl_model.py
│ ├── optimizer.py
│ ├── compare.py
│ ├── compile_ai.py
│
├── samples/
│ ├── prog1.c
│ ├── prog2.c
│ ├── prog3.c
│
├── model/
├── main.py
├── dashboard.py

##  How to Run

###  Run AI Compiler
```bash
python main.py samples/prog1.cp
python -m streamlit run dashboard.py
```
## Output
1. AI selects the best optimization level automatically
2. Execution time is measured
3. Graph compares performance across O0, O1, O2, O3

## Deep Learning Model
Input: IR-based features (10 features)
Model: Feedforward Neural Network
Output: Best optimization level

## Continuous Learning

The system improves over time by:
1. Learning from execution results
2. Updating the model after each run

## Future Scope
1. Custom LLVM Pass Integration
2. Advanced Deep Learning Models
3. Web Deployment
4. Energy Optimization
