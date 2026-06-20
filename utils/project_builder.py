import json
import os
from agents.file_planner_agent import plan_files
from agents.file_generator_agent import generate_file

def build_project(architecture):
    files=plan_files(architecture)
    for filepath in files:
        code=generate_file(filepath, architecture)
        full_path=os.path.join("generated_code",filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path,"w",encoding="utf-8") as f:
            f.write(code)
        print(f"Generated {filepath}")