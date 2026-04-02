import re

def extract_ir_features(file):
    with open(file, 'r') as f:
        ir = f.read()

    return {
        "add": len(re.findall(r'\badd\b', ir)),
        "mul": len(re.findall(r'\bmul\b', ir)),
        "load": len(re.findall(r'\bload\b', ir)),
        "store": len(re.findall(r'\bstore\b', ir)),
        "br": len(re.findall(r'\bbr\b', ir)),
        "call": len(re.findall(r'\bcall\b', ir)),
        "alloca": len(re.findall(r'\balloca\b', ir)),
        "loops": len(re.findall(r'br label', ir)),
        "functions": len(re.findall(r'define', ir)),
        "returns": len(re.findall(r'ret', ir))
    }