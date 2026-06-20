import json

from agents.file_planner_agent import (
    plan_files
)

with open(
    "generated_projects/architecture.json",
    "r",
    encoding="utf-8"
) as f:

    architecture = json.load(f)

files = plan_files(
    architecture
)

print(files)