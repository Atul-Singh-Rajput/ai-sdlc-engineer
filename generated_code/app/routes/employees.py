from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.repositories import employee_repository
from typing import List

router = APIRouter(tags=["employees"])

@router.get("/employees/", response_model=List[schemas.Employee])
def read_employees(db: Session = Depends(employee_repository.get_db)):
    employees = employee_repository.get_employees(db)
    return employees

@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(employee_repository.get_db)):
    db_employee = employee_repository.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(employee_repository.get_db)):
    db_employee = employee_repository.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    return employee_repository.create_employee(db=db, employee=employee)

@router.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(employee_repository.get_db)):
    db_employee = employee_repository.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_repository.update_employee(db=db, employee_id=employee_id, employee=employee)

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(employee_repository.get_db)):
    db_employee = employee_repository.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee_repository.delete_employee(db, employee_id=employee_id)
    return {"message": "Employee deleted successfully"}