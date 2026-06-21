from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from typing import List, Optional

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Authentication(Base):
    __tablename__ = "authentications"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

class AuthenticationRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Authentication]:
        return self.session.query(Authentication).all()

    def get_by_id(self, id: int) -> Optional[Authentication]:
        return self.session.query(Authentication).filter(Authentication.id == id).first()

    def create(self, username: str, password: str) -> Authentication:
        db_auth = Authentication(username=username, password=password)
        self.session.add(db_auth)
        self.session.commit()
        self.session.refresh(db_auth)
        return db_auth

    def update(self, id: int, username: str, password: str) -> Optional[Authentication]:
        db_auth = self.get_by_id(id)
        if db_auth:
            db_auth.username = username
            db_auth.password = password
            self.session.commit()
            self.session.refresh(db_auth)
            return db_auth
        return None

    def delete(self, id: int) -> Optional[Authentication]:
        db_auth = self.get_by_id(id)
        if db_auth:
            self.session.delete(db_auth)
            self.session.commit()
            return db_auth
        return None