import json

from agents.file_generator_agent import (
    generate_file
)

from agents.project_spec_agent import (
    generated_project_spec
)

with open(
    "generated_projects/architecture.json",
    "r",
    encoding="utf-8"
) as f:

    architecture = json.load(f)

spec = generated_project_spec(
    architecture
)

result = generate_file(
    "app/routes/employees.py",
    architecture,
    spec
)

print(result)