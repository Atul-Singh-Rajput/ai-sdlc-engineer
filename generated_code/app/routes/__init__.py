from fastapi import APIRouter
from generated_code.app.repositories import employee_repository, admin_repository, report_repository
from generated_code.app.schemas import employee, admin, report

router = APIRouter()

employees_router = APIRouter(prefix="/employees")
admins_router = APIRouter(prefix="/admins")
reports_router = APIRouter(prefix="/reports")

# Employees Routes
@employees_router.get("/")
async def read_all_employees():
    return employee_repository.get_all()

@employees_router.get("/{employee_id}")
async def read_employee(employee_id: int):
    return employee_repository.get_by_id(employee_id)

@employees_router.post("/")
async def create_employee(new_employee: employee.Employee):
    return employee_repository.create(new_employee)

@employees_router.put("/{employee_id}")
async def update_employee(employee_id: int, updated_employee: employee.Employee):
    return employee_repository.update(employee_id, updated_employee)

@employees_router.delete("/{employee_id}")
async def delete_employee(employee_id: int):
    return employee_repository.delete(employee_id)

# Admins Routes
@admins_router.get("/")
async def read_all_admins():
    return admin_repository.get_all()

@admins_router.get("/{admin_id}")
async def read_admin(admin_id: int):
    return admin_repository.get_by_id(admin_id)

@admins_router.post("/")
async def create_admin(new_admin: admin.Admin):
    return admin_repository.create(new_admin)

@admins_router.put("/{admin_id}")
async def update_admin(admin_id: int, updated_admin: admin.Admin):
    return admin_repository.update(admin_id, updated_admin)

@admins_router.delete("/{admin_id}")
async def delete_admin(admin_id: int):
    return admin_repository.delete(admin_id)

# Reports Routes
@reports_router.get("/")
async def read_all_reports():
    return report_repository.get_all()

@reports_router.get("/{report_id}")
async def read_report(report_id: int):
    return report_repository.get_by_id(report_id)

@reports_router.post("/")
async def create_report(new_report: report.Report):
    return report_repository.create(new_report)

@reports_router.put("/{report_id}")
async def update_report(report_id: int, updated_report: report.Report):
    return report_repository.update(report_id, updated_report)

@reports_router.delete("/{report_id}")
async def delete_report(report_id: int):
    return report_repository.delete(report_id)

router.include_router(employees_router)
router.include_router(admins_router)
router.include_router(reports_router)