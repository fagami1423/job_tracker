import httpx
import json
from typing import List
from docx import Document
from motor.motor_asyncio import AsyncIOMotorClient
from models import user, company

def extract_responses(json_string):
    # Split the string into individual JSON objects
    json_objects = json_string.strip().split('\n')

    # Parse each JSON object and extract the 'response' field
    responses = [json.loads(obj)["response"] for obj in json_objects if obj]

    # Concatenate all responses into a single string
    combined_response = ''.join(responses)
    return combined_response


async def insert_company(db: AsyncIOMotorClient, company_data: company.Company):
    company_dict = company_data.dict()
    company_dict.pop("description", None)  # Remove the description
    await db["companies"].insert_one(company_dict)
    
async def generate_resume(user_id: int,  db: AsyncIOMotorClient, job_description: str):
    personal_details = await db["personal_details"].find_one({"user_id": user_id})
    work_history = await db["workhistory"].find({"user_id": user_id}).to_list(None)
        # Check if data is found
    if not personal_details or not work_history:
        raise ValueError("Personal details or work history not found for the user")

    # Serialize MongoDB documents (convert ObjectId and other non-serializable fields)
    personal_details_str = json.dumps(personal_details, default=str)
    work_history_str = json.dumps([item for item in work_history], default=str)

    # Construct the prompt using the details
    prompt = f"{job_description}\""" \n generate a resume using following criteria\n"
    prompt += f"---\nBased on above job description generate a resume a resume using following criteria.\n"
    prompt += f"The resume must be in first person:\n\n"
    prompt += f"-Use these information on the top in resume format\n: {personal_details_str}\n"
    prompt += f"-Use Summary in the first section in first person\n"
    prompt += f"-Use Skills in the second section, the skills should be only the comma separated\n"
    prompt += f"-Use Experiences in the third section using the following work list \n: {work_history_str}\n add four bullet points for each list\n"
    prompt += f"-Use Education in the fourth section\n Note: I don't want any decorations no extra symbols"
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:11434/api/generate", json={"model":"orca-mini","prompt": prompt})
        generated_resume = response.text
    
    combined_response = extract_responses(generated_resume)
    print(combined_response)
    return combined_response

async def generate_cover():
    return "generate cover Coming "
# async def generate_resume(description: str):
#     async with httpx.AsyncClient() as client:
#         response = await client.post("http://localhost:11434/api/generate", json={"model":"orca-mini","prompt": description})
#         return response.text
    
def save_to_docx(content: str, file_name: str):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(file_name)
    
