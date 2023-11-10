from fastapi import APIRouter, Depends
from utils.helper import get_db
router = APIRouter()

# Dependency to get the database session
# async def get_db():
#     db = await get_database()
#     try:
#         yield db
#         print("DB connected Successfully")
#     finally:
#         # Here you can close the connection if needed
#         pass

@router.post("/")
async def create_job_application(db=Depends(get_db)):
    # Your async logic here
    get_db()
    pass

# More CRUD operations...
# @router.post("/", response_description="Add new job application", response_model=JobApplicationModel)
# async def create_job_application(job_application: JobApplicationModel = Body(...), db: AsyncIOMotorDatabase = Depends(get_db)):
#     job_application = jsonable_encoder(job_application)
#     new_job_application = await db["job_applications"].insert_one(job_application)
#     created_job_application = await db["job_applications"].find_one({"_id": new_job_application.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_job_application)