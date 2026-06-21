from fastapi import APIRouter, Depends
from generated_code.app.repositories import AuthenticationRepository
from generated_code.app.schemas import Authentication as AuthenticationSchema
from generated_code.app.database import get_db

router = APIRouter(
    prefix="/authentication",
    tags=["authentication"]
)

@router.get("/all")
async def get_all_authentications(repository: AuthenticationRepository = Depends()):
    return repository.get_all()

@router.get("/{id}")
async def get_authentication_by_id(id: int, repository: AuthenticationRepository = Depends()):
    return repository.get_by_id(id)

@router.post("/")
async def create_authentication(authentication: AuthenticationSchema, repository: AuthenticationRepository = Depends(), db = Depends(get_db)):
    return repository.create(authentication, db)

@router.put("/{id}")
async def update_authentication(id: int, authentication: AuthenticationSchema, repository: AuthenticationRepository = Depends(), db = Depends(get_db)):
    return repository.update(id, authentication, db)

@router.delete("/{id}")
async def delete_authentication(id: int, repository: AuthenticationRepository = Depends(), db = Depends(get_db)):
    return repository.delete(id, db)