from agents.code_validator_agent import (
    validate_project
)

issues = validate_project(
    "generated_code"
)

for issue in issues:

    print(
        issue
    )