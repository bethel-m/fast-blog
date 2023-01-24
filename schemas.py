from pydantic import BaseModel
from typing import Optional
class Blog(BaseModel):
  title: str 
  body: str
  
class ShowBlog(BaseModel):
  title: str 
  body: str
  class Config:
    orm_mode = True
    
class User(BaseModel):
  name: str
  email: str
  password: str