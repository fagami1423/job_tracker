from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from .security import verify_password
from .config import settings

# To get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(fake_db, email: str, password: str):
    user = fake_db.get(email)
    if not user:
        return False
    if not verify_password(password, user['hashed_password']):
        return False
    return user
