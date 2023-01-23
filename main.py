from fastapi import FastAPI,Depends
import schemas,models
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

@app.post("/blog")
def create_blog(request: schemas.Blog,db: session = Depends(get_db)):
  new_blog = models.Blog(title=request.title,body=request.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog