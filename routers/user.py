from fastapi import APIRouter,Depends,HTTPException,status
import schemas,models,hashing,database
from sqlalchemy.orm import session
from repositories import user


router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.post("/",response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: session = Depends(database.get_db)):
  return user.create_user(request,db)

@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id: int,db: session = Depends(database.get_db)):
  return user.get_user(id,db)
