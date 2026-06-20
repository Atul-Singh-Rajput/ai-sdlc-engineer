from fastapi import FastAPI
from generated_code.app.routes import employees, departments, reporting, auth

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(departments.router, prefix="/departments", tags=["departments"])
app.include_router(reporting.router, prefix="/reporting", tags=["reporting"])
app.include_router(auth.router, prefix="/authentication", tags=["authentication"])