from pydantic import BaseModel, EmailStr

# User in DB model should also inherit from Pydantic's `BaseModel`
class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    disabled: bool = False

# User model for registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# User model for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
