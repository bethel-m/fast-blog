from sqlalchemy.orm import session
from fastapi import HTTPException,status
import models
import schemas


def create_blog(request: schemas.Blog,db: session,user_id:int):
  new_blog = models.Blog(title=request.title,body=request.body,user_id=user_id)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def all(db: session):
  blogs = db.query(models.Blog).all()
  return blogs
  
def get(id:int,db: session):
  blog = db.query(models.Blog).filter(models.Blog.id==id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog for id {id} not found")
  return blog

def destroy(id: int,db: session):
  query = db.query(models.Blog).filter(models.Blog.id==id)
  if not query.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog for id {id} not found")
  query.delete(synchronize_session=False)
  db.commit()
  return  {"detail":f"post with id {id} deleted"}