from agents.requirement_agent import analyze_requirement

result= analyze_requirement(
    """ Build Employee Management System
    Admin can create employees
    update employees
    assign department
    generate reports
    """
)

print(result)