from fastapi import APIRouter,status,Depends
from typing import List
from sqlalchemy.orm import session
from repositories import blog
from database import get_db
from oauth2 import get_current_user
import schemas


router = APIRouter(
  prefix="/blog",
  tags=["Blogs"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,db: session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
  return blog.create_blog(request,db)

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def all(db:session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
  return blog.all(db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id: int,db: session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
  return blog.get(id,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db: session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
  return blog.destroy(id,db)