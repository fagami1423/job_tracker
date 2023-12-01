from motor.motor_asyncio import AsyncIOMotorClient

# Initialization script or startup event in FastAPI
async def initialize_counters(db: AsyncIOMotorClient):
    user_counter = await db["counters"].find_one({"_id": "user_id"})
    if not user_counter:
        await db["counters"].insert_one({"_id": "user_id", "sequence_value": 0})


async def get_next_sequence_value(db: AsyncIOMotorClient, sequence_name: str):
    result = await db["counters"].find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        return_document=True
    )
    return result["sequence_value"]

