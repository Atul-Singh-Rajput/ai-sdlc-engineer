import json

from utils.project_builder import (
    build_project
)

with open(
    "generated_projects/architecture.json",
    "r",
    encoding="utf-8"
) as f:

    architecture = json.load(f)

build_project(
    architecture
)