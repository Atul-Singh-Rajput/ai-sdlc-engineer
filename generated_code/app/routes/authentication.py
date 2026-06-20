from fastapi import APIRouter, Depends
from generated_code.app.repositories import AuthenticationRepository
from app import database

router = APIRouter(prefix="/authentication", tags=["Authentication"])

@router.get("/get_all")
async def get_all_authentications(auth_repo: AuthenticationRepository = Depends()):
    return auth_repo.get_all()

@router.get("/get_by_id/{id}")
async def get_authentication_by_id(id: int, auth_repo: AuthenticationRepository = Depends()):
    return auth_repo.get_by_id(id)

@router.post("/create")
async def create_authentication(authentication: dict, auth_repo: AuthenticationRepository = Depends()):
    return auth_repo.create(authentication)

@router.put("/update/{id}")
async def update_authentication(id: int, authentication: dict, auth_repo: AuthenticationRepository = Depends()):
    return auth_repo.update(id, authentication)

@router.delete("/delete/{id}")
async def delete_authentication(id: int, auth_repo: AuthenticationRepository = Depends()):
    return auth_repo.delete(id)