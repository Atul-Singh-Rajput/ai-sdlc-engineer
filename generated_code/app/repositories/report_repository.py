from sqlalchemy import select
from generated_code.app.models import Report
from generated_code.app.database import SessionLocal
from typing import List

class ReportRepository:
    def __init__(self, session: SessionLocal):
        self.session = session

    def get_all(self) -> List[Report]:
        return self.session.execute(select(Report)).all()

    def get_by_id(self, id: int) -> Report:
        return self.session.get(Report, id)

    def create(self, report: Report) -> Report:
        self.session.add(report)
        self.session.commit()
        self.session.refresh(report)
        return report

    def update(self, id: int, report: Report) -> Report:
        existing_report = self.get_by_id(id)
        if existing_report:
            existing_report.name = report.name
            existing_report.content = report.content
            self.session.commit()
            self.session.refresh(existing_report)
            return existing_report
        return None

    def delete(self, id: int) -> bool:
        report = self.get_by_id(id)
        if report:
            self.session.delete(report)
            self.session.commit()
            return True
        return False