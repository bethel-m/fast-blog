from fastapi import FastAPI,Depends,status,HTTPException
import schemas,models
from typing import List
from database import engine,SessionLocal
from sqlalchemy.orm import session

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close

models.Base.metadata.create_all(engine)

@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,db: session = Depends(get_db)):
  new_blog = models.Blog(title=request.title,body=request.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

@app.get("/get",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def all(db:session = Depends(get_db)):
  blogs = db.query(models.Blog).all()
  return blogs

@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id,db: session = Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id==id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog for id {id} not found")
  return blog

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: session = Depends(get_db)):
  db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
  db.commit()
  return {"detail":f"post with id {id} deleted"}

@app.post("/user")
def create_user(request: schemas.User,db: session = Depends(get_db)):
  new_user = models.User(name=request.name,email=request.email,password=request.password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user
