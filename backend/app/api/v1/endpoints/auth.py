from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from core.auth import create_access_token, authenticate_user, get_current_user
from core.security import get_password_hash
from models.user import UserInDB, UserCreate, UserLogin, PersonalDetails,WorkHistoryItem
from core.config import settings
from utils.helper import get_database
from utils.auto_increment import get_next_sequence_value
from fastapi import HTTPException
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate, db: AsyncIOMotorClient = Depends(get_database)):
    # Check if the user already exists
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Get the next user_id
    user_id = await get_next_sequence_value(db, "user_id")
    
    # Create a new user with hashed password
    hashed_password = get_password_hash(user.password)
    user_db = UserInDB(**user.dict(), hashed_password=hashed_password, user_id=user_id)

    # Save the user in the database
    await db["users"].insert_one(user_db.dict(by_alias=True))
    

    # Return the created user (excluding hashed password)
    return {"username": user_db.username, "email": user_db.email}

@router.post("/login")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: AsyncIOMotorClient = Depends(get_database)
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user['email']},  # Assuming the email is stored under 'email' key
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@router.post("/personal_details/")
async def add_personal_details(details: PersonalDetails, db: AsyncIOMotorClient = Depends(get_database), current_user: UserInDB = Depends(get_current_user)):
    user_id = current_user.get("use_id")
    existing_details = await db["personal_details"].find_one({"user_id": user_id})

    if existing_details:
        # Handle the duplicate case - either reject, update, or other logic
        raise HTTPException(status_code=400, detail="Personal details for this user already exist")

    # If no existing details, proceed to add new details
    details_dict = details.dict()
    result = await db["personal_details"].insert_one(details_dict)
    created_details = await db["personal_details"].find_one({"_id": result.inserted_id})
    
    # Convert ObjectId to string
    created_details["_id"] = str(created_details["_id"])
    
    return JSONResponse(content=created_details)
    


@router.post("/work_history/")
async def add_work_history(history: WorkHistoryItem, db: AsyncIOMotorClient = Depends(get_database),current_user: UserInDB = Depends(get_current_user)):
    # Logic to save work history
    user_id = current_user.get("user_id")
    history_dict = history.dict()
    history_dict["user_id"] = user_id
    result = await db["workhistory"].insert_one(history_dict)
    created_history = await db["workhistory"].find_one({"_id": result.inserted_id})
    
    # Convert ObjectId to string
    created_history["_id"] = str(created_history["_id"])
    
    return JSONResponse(content=created_history)