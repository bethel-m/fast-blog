from hashing import Hash
from sqlalchemy.orm import session
from fastapi import HTTPException,status
import models
import schemas


def create_user(request: schemas.User,db: session):
  hashed_password = Hash.bcrypt(request.password)
  new_user = models.User(name=request.name,email=request.email,password=hashed_password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


def get_user(id:int,db:session):
  query = db.query(models.User).filter(models.User.id == id).first()
  if not query:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} does not exist")
  return query