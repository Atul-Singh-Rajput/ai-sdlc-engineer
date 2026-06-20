from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generated_code.app.models import Report
from generated_code.app.database import engine

class ReportRepository:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all(self):
        return self.session.query(Report).all()

    def get_by_id(self, id: int):
        return self.session.query(Report).filter(Report.id == id).first()

    def create(self, report: Report):
        self.session.add(report)
        self.session.commit()
        self.session.refresh(report)
        return report

    def update(self, id: int, report: Report):
        existing_report = self.get_by_id(id)
        if existing_report:
            existing_report.name = report.name
            existing_report.description = report.description
            self.session.commit()
            self.session.refresh(existing_report)
            return existing_report
        else:
            return None

    def delete(self, id: int):
        report = self.get_by_id(id)
        if report:
            self.session.delete(report)
            self.session.commit()
            return True
        else:
            return False