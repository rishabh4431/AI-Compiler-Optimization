import sys
from backend.compile_ai import compile_ai
from backend.compare import compare

if len(sys.argv) < 2:
    print("Usage: python main.py <file.c>")
else:
    compile_ai(sys.argv[1])