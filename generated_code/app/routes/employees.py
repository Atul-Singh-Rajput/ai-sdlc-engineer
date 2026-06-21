from fastapi import APIRouter, Depends
from generated_code.app.repositories import EmployeeRepository
from generated_code.app.schemas import Employee
from generated_code.app.database import SessionLocal

router = APIRouter(prefix="/employees")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_all_employees(db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    return employee_repository.get_all()

@router.get("/{employee_id}")
async def get_by_id(employee_id: int, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    return employee_repository.get_by_id(employee_id)

@router.post("/")
async def create(employee: Employee, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    return employee_repository.create(employee)

@router.put("/{employee_id}")
async def update(employee_id: int, employee: Employee, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    return employee_repository.update(employee_id, employee)

@router.delete("/{employee_id}")
async def delete(employee_id: int, db: SessionLocal = Depends(get_db)):
    employee_repository = EmployeeRepository(db)
    return employee_repository.delete(employee_id)