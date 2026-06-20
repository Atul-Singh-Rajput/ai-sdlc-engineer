from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from generated_code.app.config.database import DATABASE_URL
from sqlalchemy.orm import Session

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Authentication(Base):
    __tablename__ = "authentications"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class AuthenticationRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Authentication).all()

    def get_by_id(self, id: int):
        return self.session.query(Authentication).filter(Authentication.id == id).first()

    def create(self, authentication: dict):
        new_authentication = Authentication(**authentication)
        self.session.add(new_authentication)
        self.session.commit()
        self.session.refresh(new_authentication)
        return new_authentication

    def update(self, id: int, authentication: dict):
        existing_authentication = self.get_by_id(id)
        if existing_authentication:
            existing_authentication.username = authentication.get("username")
            existing_authentication.password = authentication.get("password")
            self.session.commit()
            self.session.refresh(existing_authentication)
            return existing_authentication
        return None

    def delete(self, id: int):
        existing_authentication = self.get_by_id(id)
        if existing_authentication:
            self.session.delete(existing_authentication)
            self.session.commit()
            return True
        return False