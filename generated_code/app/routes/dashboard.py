from fastapi import APIRouter
from generated_code.app.repositories import EmployeeRepository
from generated_code.app.schemas import Employee

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/employees-count")
async def get_employees_count():
    employee_repository = EmployeeRepository()
    return {"employees_count": await employee_repository.get_all()}

@router.get("/employees-report")
async def get_employees_report():
    employee_repository = EmployeeRepository()
    employees = await employee_repository.get_all()
    report = []
    for employee in employees:
        report.append({"id": employee.id, "name": employee.name})
    return report