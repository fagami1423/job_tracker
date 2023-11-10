import motor.motor_asyncio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the database details from the environment variable
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

# Create a client instance
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Function to fetch the database
async def get_database():
    return client.Cluster0  # Replace 'your_db_name' with your actual database name
