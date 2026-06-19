from agents.architecture_agent import generate_architecture
sample={
    "Project Name": "Employee Management System",
    "Entities":["Employee","Department"],
    "Features":["Create Employee","Update Employee"]
}

result= generate_architecture(sample)
print(result)