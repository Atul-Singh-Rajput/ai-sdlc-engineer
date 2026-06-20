from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from generated_code.app.repositories.department_repository import DepartmentRepository
from generated_code.app.schemas.department import Department

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)

@router.get("/", response_model=List[Department])
async def read_departments(department_repository: DepartmentRepository = Depends()):
    return department_repository.get_all()

@router.get("/{department_id}", response_model=Department)
async def read_department(department_id: int, department_repository: DepartmentRepository = Depends()):
    department = department_repository.get_by_id(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.post("/", response_model=Department)
async def create_department(department: Department, department_repository: DepartmentRepository = Depends()):
    return department_repository.create(department)

@router.put("/{department_id}", response_model=Department)
async def update_department(department_id: int, department: Department, department_repository: DepartmentRepository = Depends()):
    existing_department = department_repository.get_by_id(department_id)
    if existing_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department_repository.update(department_id, department)

@router.delete("/{department_id}")
async def delete_department(department_id: int, department_repository: DepartmentRepository = Depends()):
    department = department_repository.get_by_id(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    department_repository.delete(department_id)
    return {"message": "Department deleted successfully"}