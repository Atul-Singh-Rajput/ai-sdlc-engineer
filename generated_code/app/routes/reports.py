from fastapi import APIRouter, Depends, HTTPException
from generated_code.app.repositories import ReportRepository
from generated_code.app.schemas import Report
from generated_code.app.database import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_all_reports(report_repository: ReportRepository = Depends()):
    return report_repository.get_all()

@router.get("/{report_id}")
async def read_report(report_id: int, report_repository: ReportRepository = Depends()):
    report = report_repository.get_by_id(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

@router.post("/")
async def create_report(report: Report, report_repository: ReportRepository = Depends()):
    return report_repository.create(report)

@router.put("/{report_id}")
async def update_report(report_id: int, report: Report, report_repository: ReportRepository = Depends()):
    existing_report = report_repository.get_by_id(report_id)
    if existing_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report_repository.update(report_id, report)

@router.delete("/{report_id}")
async def delete_report(report_id: int, report_repository: ReportRepository = Depends()):
    report_repository.delete(report_id)
    return {"message": "Report deleted successfully"}