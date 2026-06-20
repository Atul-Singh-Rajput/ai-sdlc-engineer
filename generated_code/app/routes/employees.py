from fastapi import APIRouter, Depends, HTTPException
from generated_code.app.repositories.employee_repository import EmployeeRepository
from generated_code.app.schemas.employee import Employee, EmployeeCreate, EmployeeUpdate
from generated_code.app.database import SessionLocal

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Employee])
def read_employees(db: SessionLocal = Depends(get_db)):
    repository = EmployeeRepository(db)
    return repository.get_all()

@router.get("/{employee_id}", response_model=Employee)
def read_employee(employee_id: int, db: SessionLocal = Depends(get_db)):
    repository = EmployeeRepository(db)
    employee = repository.get_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: SessionLocal = Depends(get_db)):
    repository = EmployeeRepository(db)
    return repository.create(employee)

@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: SessionLocal = Depends(get_db)):
    repository = EmployeeRepository(db)
    employee_db = repository.get_by_id(employee_id)
    if employee_db is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return repository.update(employee_id, employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: SessionLocal = Depends(get_db)):
    repository = EmployeeRepository(db)
    employee = repository.get_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    repository.delete(employee_id)
    return {"message": "Employee deleted"}