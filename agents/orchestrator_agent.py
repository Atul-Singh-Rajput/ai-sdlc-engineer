import json

from agents.requirement_agent import (
    analyze_requirement
)

from agents.architecture_agent import (
    generate_architecture
)

from agents.project_spec_agent import (
    generated_project_spec
)

from utils.project_builder import (
    build_project
)

from agents.auto_fix_agent import (
    auto_fix
)

from agents.code_validator_agent import (
    validate_project
)


def run_pipeline(
    requirement
):

    print(
        "\nSTEP 1: Requirement Analysis"
    )

    analysis = analyze_requirement(
        requirement
    )

    print(
        "Completed"
    )

    print(
        "\nSTEP 2: Architecture"
    )

    architecture = generate_architecture(
        analysis
    )

    print(
        "Completed"
    )

    print(
        "\nSTEP 3: Project Spec"
    )

    spec = generated_project_spec(
        architecture
    )

    print(
        "Completed"
    )

    print(
        "\nSTEP 4: Build Project"
    )

    build_project(
        architecture
    )

    print(
        "Completed"
    )

    print(
        "\nSTEP 5: Auto Fix"
    )

    auto_fix(
        "generated_code"
    )

    print(
        "Completed"
    )

    print(
        "\nSTEP 6: Validation"
    )

    issues = validate_project(
        "generated_code"
    )

    print(
        "Completed"
    )

    return {

        "analysis":
        analysis,

        "architecture":
        architecture,

        "spec":
        spec,

        "issues":
        issues
    }