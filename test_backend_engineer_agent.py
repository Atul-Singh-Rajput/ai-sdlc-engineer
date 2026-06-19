import json
from agents.backend_engineer_agent import generate_backend_code
with open("generated_projects/architecture.json","r",encoding="utf-8") as f:
    architecture = json.load(f)

result = generate_backend_code(architecture)
print(result)