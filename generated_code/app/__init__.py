from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from generated_code.app.routes import employees, admins, reports
from generated_code.app.database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(admins.router, prefix="/admins", tags=["admins"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])