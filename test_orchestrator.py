from agents.orchestrator_agent import (
    run_pipeline
)

result = run_pipeline(

    """
    Build Employee Management System

    Features:

    Employee CRUD
    Department CRUD
    Reporting Dashboard
    Authentication
    """
)

print(result)