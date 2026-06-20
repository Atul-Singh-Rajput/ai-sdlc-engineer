import json
def generated_project_spec(architecture):
  modules=architecture.get(
    "modules",
    [])
  spec={}
  for module in modules:
    singular=module.rstrip("s")
    spec[module]={
      "model_name":singular.capitalize(),
      "repository_name":f"{singular.capitalize()}Repository",
      "schema_name":singular.capitalize(),
      "route_prefix":f"/{module}",
      "repository_methods":[
        "get_all",
        "get_by_id",
        "create",
        "update",
        "delete"
      ]
     }
    return spec