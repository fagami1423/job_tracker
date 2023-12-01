from models.user import UserCreate, UserInDB
from core.security import get_password_hash
from utils.auto_increment import get_next_sequence_value

async def migrate_initial_users(db,users: list[UserCreate]):
    for user_data in users:
        # Check if user already exists
        if await db["users"].find_one({"email": user_data.email}):
            continue

        # Get the next user_id
        user_id = await get_next_sequence_value(db, "user_id")
        # Hash the password
        hashed_password = get_password_hash(user_data.password)
        
        # Create a UserInDB instance
        user_in_db = UserInDB(
            **user_data.dict(exclude={"password"}), 
            hashed_password=hashed_password,
            user_id = user_id
        )

        # Insert into the database
        await db["users"].insert_one(user_in_db.dict())
