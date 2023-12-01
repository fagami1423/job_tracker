from fastapi import FastAPI
from core.migrate import migrate_initial_users
from app.api.v1.endpoints import job_application, company, auth,resume
from models.user import UserCreate
from utils.auto_increment import initialize_counters
from utils.helper import get_database


app = FastAPI(
    title="Job Tracking Application",
    description="API for accessing data from of BESS"
    
)

@app.on_event("startup")
async def startup_event():
    db = await get_database()
    initial_users = [
        UserCreate(username="admin1", email="admin1@example.com", password="admin123"),
        UserCreate(username="admin2", email="admin2@example.com", password="password123"),
        # Add more users as needed
    ]
    await initialize_counters(db)
    await migrate_initial_users(db,initial_users)


# Register API routers
# app.include_router(job_application.router, prefix="/api/v1/job_application", tags=["Job Application"])
app.include_router(resume.router, prefix="/api/v1/company", tags=["Resume"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["User"])
