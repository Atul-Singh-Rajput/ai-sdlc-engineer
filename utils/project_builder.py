import os
import shutil
from agents.file_planner_agent import (
    plan_files
)

from agents.file_generator_agent import (
    generate_file
)

from agents.project_spec_agent import (
    generated_project_spec
)

def build_project(
    architecture
):
    if os.path.exists(
        "generated_code"
    ):
        shutil.rmtree(
            "generated_code"
        )
    spec = generated_project_spec(
        architecture
    )

    files = plan_files(
        architecture
    )

    for filepath in files:

        content = generate_file(
            filepath,
            architecture,
            spec
        )

        full_path = os.path.join(
            "generated_code",
            filepath
        )

        os.makedirs(
            os.path.dirname(full_path),
            exist_ok=True
        )

        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                content
            )

        print(
            f"Generated {filepath}"
        )