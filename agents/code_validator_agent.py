import os
import re
import ast

def get_repository_methods(filepath):

    methods = []

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        tree = ast.parse(
            f.read()
        )

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.FunctionDef
        ):

            methods.append(
                node.name
            )

    return methods

def get_route_method_calls(filepath):

    calls = []

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    matches = re.findall(
        r"employee_repository\.([a-zA-Z_][a-zA-Z0-9_]*)\(",
        content
    )

    calls.extend(matches)

    return calls


def validate_project(project_root):

    issues = []


    for root, dirs, files in os.walk(project_root):

        for file in files:

            if not file.endswith(".py"):
                continue

            filepath = os.path.join(root, file)

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            # Invalid imports

            if "from app." in content:

                issues.append({
                    "file": filepath,
                    "issue": "Invalid import path"
                })

            imports = re.findall(
                r"from\s+([a-zA-Z0-9_\.]+)\s+import",
                content
            )

            for imp in imports:

                if "services" in imp:

                    issues.append({
                        "file": filepath,
                        "issue": f"Missing dependency: {imp}"
                    })



    repo_file = os.path.join(
        project_root,
        "app",
        "repositories",
        "employee_repository.py"
    )

    route_file = os.path.join(
        project_root,
        "app",
        "routes",
        "employees.py"
    )

    if (
        os.path.exists(repo_file)
        and
        os.path.exists(route_file)
    ):

        repo_methods = get_repository_methods(
            repo_file
        )

        route_calls = get_route_method_calls(
            route_file
        )

        for call in route_calls:

            if (
                call.startswith("get")
                or call.startswith("create")
                or call.startswith("update")
                or call.startswith("delete")
            ):

                if call not in repo_methods:

                    issues.append({

                        "file": route_file,

                        "issue":
                        f"Repository method missing: {call}"

                    })

    return issues