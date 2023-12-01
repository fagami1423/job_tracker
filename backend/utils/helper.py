from db.mongodb import get_database

# Dependency to get the database session
async def get_db():
    db = await get_database()
    try:
        yield db
        print("DB connected Successfully")
    finally:
        # Here you can close the connection if needed
        pass
    
