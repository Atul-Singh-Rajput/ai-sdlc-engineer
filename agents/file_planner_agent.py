import json
def plan_files(architecture):
    modules=architecture.get("modules",[])
    files=["app/main.py"]
    for module in modules:
        files.append(f"app/routes/{module}.py")
    return files