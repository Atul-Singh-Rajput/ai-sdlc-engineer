import json
def plan_files(architecture):

    modules = architecture.get(
        "modules",
        []
    )

    files = [
        "app/main.py"
    ]

    for module in modules:

        module_name = module.rstrip("s")

        files.append(
            f"app/routes/{module}.py"
        )

        files.append(
            f"app/models/{module_name}.py"
        )

        files.append(
            f"app/schemas/{module_name}.py"
        )

        files.append(
            f"app/repositories/{module_name}_repository.py"
        )

    return files