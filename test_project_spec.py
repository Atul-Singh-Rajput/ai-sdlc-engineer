import json

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

print(
    json.dumps(
        spec,
        indent=4
    )
)