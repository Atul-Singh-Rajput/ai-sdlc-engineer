from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Authentication(Base):
    __tablename__ = "authentications"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Authentication(id={self.id}, username={self.username}, password={self.password}, is_active={self.is_active})"