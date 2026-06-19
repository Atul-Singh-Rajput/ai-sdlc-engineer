import json
import os

from agents.backend_engineer_agent import (
    generate_backend_code
)

with open(
    "generated_projects/architecture.json",
    "r",
    encoding="utf-8"
) as f:

    architecture = json.load(f)

code = generate_backend_code(
    architecture
)

os.makedirs(
    "generated_code/app",
    exist_ok=True
)

with open(
    "generated_code/app/main.py",
    "w",
    encoding="utf-8"
) as f:

    f.write(code)

print(
    "main.py generated successfully"
)