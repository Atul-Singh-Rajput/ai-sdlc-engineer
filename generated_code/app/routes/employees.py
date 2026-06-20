from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import Employee
from app.services.employee_service import EmployeeService

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

@router.get("/")
async def get_all_employees(employee_repository: EmployeeRepository = Depends()):
    employees = await employee_repository.get_all()
    return JSONResponse(content=[employee.dict() for employee in employees], status_code=status.HTTP_200_OK)

@router.get("/{employee_id}")
async def get_employee_by_id(employee_id: int, employee_repository: EmployeeRepository = Depends()):
    employee = await employee_repository.get_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return JSONResponse(content=employee.dict(), status_code=status.HTTP_200_OK)

@router.post("/")
async def create_employee(employee: Employee, employee_repository: EmployeeRepository = Depends()):
    new_employee = await employee_repository.create(employee)
    return JSONResponse(content=new_employee.dict(), status_code=status.HTTP_201_CREATED)

@router.put("/{employee_id}")
async def update_employee(employee_id: int, employee: Employee, employee_repository: EmployeeRepository = Depends()):
    updated_employee = await employee_repository.update(employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return JSONResponse(content=updated_employee.dict(), status_code=status.HTTP_200_OK)

@router.delete("/{employee_id}")
async def delete_employee(employee_id: int, employee_repository: EmployeeRepository = Depends()):
    deleted_employee = await employee_repository.delete(employee_id)
    if not deleted_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return JSONResponse(content={"message": "Employee deleted successfully"}, status_code=status.HTTP_200_OK)