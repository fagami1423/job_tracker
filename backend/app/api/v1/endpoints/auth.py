from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from core.auth import create_access_token, authenticate_user
from core.security import get_password_hash
from models.user import UserInDB, UserCreate, UserLogin
from core.config import settings
from utils.helper import get_db

router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate, db=Depends(get_db)):
    # Create a new user
    hashed_password = get_password_hash(user.password)
    user_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    # Save the user in the database
    # ... Database save logic here ...
    
    return {"username": user_db.username, "email": user_db.email}

@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
