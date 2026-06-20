from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import employee_service
from app.repositories.employee_repository import employee_repository

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate):
    return employee_service.create_employee(employee)


@router.get("/", response_model=list[EmployeeResponse])
async def read_employees():
    return employee_service.read_employees()


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def read_employee(employee_id: int):
    employee = employee_service.read_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(employee_id: int, employee: EmployeeUpdate):
    existing_employee = employee_service.read_employee(employee_id)
    if not existing_employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee_service.update_employee(employee_id, employee)


@router.delete("/{employee_id}")
async def delete_employee(employee_id: int):
    employee = employee_service.read_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    employee_service.delete_employee(employee_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Employee deleted successfully"})