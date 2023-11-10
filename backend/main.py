from fastapi import FastAPI
from app.api.v1.endpoints import job_application, company, auth

app = FastAPI(
    title="Job Tracking Application",
    description="API for accessing data from of BESS"
    
)

# Register API routers
app.include_router(job_application.router, prefix="/api/v1/job_application", tags=["Job Application"])
# app.include_router(company.router, prefix="/api/v1/company", tags=["Company"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
