from fastapi import APIRouter, Depends, HTTPException
from generated_code.app.repositories.employee_repository import EmployeeRepository
from generated_code.app.schemas.employee import Employee, EmployeeCreate, EmployeeUpdate
from generated_code.app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/", response_model=list[Employee])
def read_employees(db: Session = Depends(get_db)):
    return EmployeeRepository(db).get_all()

@router.get("/{employee_id}", response_model=Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = EmployeeRepository(db).get_by_id(employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeRepository(db).create(employee)

@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = EmployeeRepository(db).get_by_id(employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return EmployeeRepository(db).update(db_employee, employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = EmployeeRepository(db).get_by_id(employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    EmployeeRepository(db).delete(db_employee)
    return {"message": f"Employee {employee_id} deleted"}