from fastapi import APIRouter, Depends
from generated_code.app.repositories import ReportingRepository
from typing import List

router = APIRouter(prefix="/reporting", tags=["Reporting"])

@router.get("/")
async def get_all_reporting(
    reporting_repository: ReportingRepository = Depends()
):
    return reporting_repository.get_all()

@router.get("/{reporting_id}")
async def get_reporting_by_id(
    reporting_id: int,
    reporting_repository: ReportingRepository = Depends()
):
    return reporting_repository.get_by_id(reporting_id)

@router.post("/")
async def create_reporting(
    reporting: dict,
    reporting_repository: ReportingRepository = Depends()
):
    return reporting_repository.create(reporting)

@router.put("/{reporting_id}")
async def update_reporting(
    reporting_id: int,
    reporting: dict,
    reporting_repository: ReportingRepository = Depends()
):
    return reporting_repository.update(reporting_id, reporting)

@router.delete("/{reporting_id}")
async def delete_reporting(
    reporting_id: int,
    reporting_repository: ReportingRepository = Depends()
):
    return reporting_repository.delete(reporting_id)