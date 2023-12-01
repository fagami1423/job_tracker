from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId

# User in DB model should also inherit from Pydantic's `BaseModel`
class UserInDB(BaseModel):
    user_id:int
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


class WorkHistoryItem(BaseModel):
    id: str = Field(None, alias="_id")
    user_id: int
    company_name: str
    position: str
    start_date: str
    end_date: str
    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }
    # Add other relevant fields

class PersonalDetails(BaseModel):
    id: str = Field(None, alias="_id")
    user_id: int
    name: str
    email: str
    phone_number: str
    address: str
    # Add other relevant fields
    
    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }


