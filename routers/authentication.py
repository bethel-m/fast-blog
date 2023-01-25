from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from database import get_db
from hashing import Hash
from JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
import schemas
import models


router = APIRouter(
  tags=["Login"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends() ,db: session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid login credentials")
  if not Hash.verify(request.password,user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid login credentials")
  
  access_token = create_access_token(
    data={"sub":user.email}
  )
  return {"access_token":access_token,"token_type":"bearer"}