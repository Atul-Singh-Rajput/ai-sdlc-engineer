from sqlalchemy import select
from generated_code.app.models import Report
from generated_code.app.database import SessionLocal
from typing import List

class ReportRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_all(self) -> List[Report]:
        return self.db.execute(select(Report)).all()

    def get_by_id(self, report_id: int) -> Report:
        return self.db.execute(select(Report).where(Report.id == report_id)).scalar()

    def create(self, report: Report) -> Report:
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def update(self, report_id: int, report: Report) -> Report:
        existing_report = self.get_by_id(report_id)
        if existing_report:
            existing_report.name = report.name
            existing_report.description = report.description
            self.db.commit()
            self.db.refresh(existing_report)
            return existing_report
        return None

    def delete(self, report_id: int) -> bool:
        report = self.get_by_id(report_id)
        if report:
            self.db.delete(report)
            self.db.commit()
            return True
        return False