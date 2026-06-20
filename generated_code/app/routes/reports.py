from fastapi import APIRouter, Depends
from generated_code.app.repositories.report_repository import ReportRepository
from generated_code.app.schemas.report import Report

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/")
async def get_all_reports(report_repository: ReportRepository = Depends()):
    return report_repository.get_all()

@router.get("/{report_id}")
async def get_report_by_id(report_id: int, report_repository: ReportRepository = Depends()):
    return report_repository.get_by_id(report_id)

@router.post("/")
async def create_report(report: Report, report_repository: ReportRepository = Depends()):
    return report_repository.create(report)

@router.put("/{report_id}")
async def update_report(report_id: int, report: Report, report_repository: ReportRepository = Depends()):
    return report_repository.update(report_id, report)

@router.delete("/{report_id}")
async def delete_report(report_id: int, report_repository: ReportRepository = Depends()):
    return report_repository.delete(report_id)