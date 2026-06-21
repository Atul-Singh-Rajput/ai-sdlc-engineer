from fastapi import FastAPI
from generated_code.app.database import engine
from generated_code.app.routes import employee_routes, report_routes, auth_routes

app = FastAPI()

app.include_router(employee_routes.router)
app.include_router(report_routes.router)
app.include_router(auth_routes.router)