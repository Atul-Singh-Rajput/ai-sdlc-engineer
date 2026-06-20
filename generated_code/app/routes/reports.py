from fastapi import APIRouter, Depends
from generated_code.app.repositories import EmployeeRepository
from generated_code.app.models import Employee
from generated_code.app.schemas import Employee as EmployeeSchema

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.get("/employees")
async def get_all_employees(employee_repository: EmployeeRepository = Depends()):
    return await employee_repository.get_all()

@router.get("/employees/{employee_id}")
async def get_employee_by_id(employee_id: int, employee_repository: EmployeeRepository = Depends()):
    return await employee_repository.get_by_id(employee_id)

@router.post("/employees")
async def create_employee(employee: EmployeeSchema, employee_repository: EmployeeRepository = Depends()):
    return await employee_repository.create(employee.dict())

@router.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: EmployeeSchema, employee_repository: EmployeeRepository = Depends()):
    return await employee_repository.update(employee_id, employee.dict())

@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int, employee_repository: EmployeeRepository = Depends()):
    return await employee_repository.delete(employee_id)