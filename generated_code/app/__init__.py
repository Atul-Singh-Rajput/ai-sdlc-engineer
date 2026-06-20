from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import List, Optional

from generated_code.app.routes import employees, departments, reporting, auth
from generated_code.app.database import engine

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(departments.router, prefix="/departments", tags=["departments"])
app.include_router(reporting.router, prefix="/reporting", tags=["reporting"])
app.include_router(auth.router, prefix="/authentication", tags=["authentication"])