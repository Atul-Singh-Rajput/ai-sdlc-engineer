import json
from agents.file_generator_agent import generate_file

with open(
    "generated_projects/architecture.json",
    "r",
    encoding="utf-8"
) as f:

    architecture = json.load(f)
result=generate_file(
    "app/repositories/employee_repository.py",
    architecture
)

print(result)