from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Dashboard(Base):
    __tablename__ = 'dashboard'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f'Dashboard(id={self.id}, title={self.title}, description={self.description})'