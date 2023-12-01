from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import APIRouter, HTTPException, Depends

from db.mongodb import get_database
from models.company import Company
from models import user
from core.auth import get_current_user
from utils.resume_generator import save_to_docx, generate_resume, generate_cover,insert_company
from fastapi import FastAPI, Form
from datetime import datetime



from pydantic import BaseModel

class ResumeRequest(BaseModel):
    company: Company  # Assuming Company is another Pydantic model
    text: str


router = APIRouter()

@router.post("/submit_form_text")
async def submit_form_text(text: str = Form(...)):
    # Process the text
    return {"received": text}

@router.post("/create_resume/{user_id}")
async def create_resume(user_id: int, company_name: str = Form(...), position: str = Form(...),website: str = Form(...), need_cover_letter: bool = Form(...), text: str = Form(...), db: AsyncIOMotorClient = Depends(get_database)):
    company = Company(name=company_name,position=position,website=website, need_cover_letter=need_cover_letter,created_date=datetime.utcnow())
    # await insert_company(db, company)

    # if company.need_cover_letter:
    #     cover_letter = await generate_cover(text)
    #     save_to_docx(cover_letter, f"{company_name}_cover_letter.docx")

    resume = await generate_resume(user_id,db,text)
    save_to_docx(resume, f"{company_name}_resume.docx")

    return {"message": "Company and documents created successfully"}