# 📋 Job Tracker with an AI Resume Generator

A FastAPI backend for tracking job applications that also **generates a tailored resume for each job description with a local LLM** (Ollama), exported as a Word document.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white)
![Ollama](https://img.shields.io/badge/LLM-Ollama-000000)

## ✨ Features
- 🔐 **JWT authentication:** register, log in and get the current user
- 👤 **Candidate profile:** store personal details and work history
- 🏢 **Companies and job applications:** keep track of where you've applied
- 🤖 **AI resume generation:** combines the job description with your stored profile and work history into a prompt for a local LLM (`orca-mini` through the Ollama API), producing a first-person, job-specific resume
- 📄 **Word export** of generated resumes with `python-docx`
- ⚡ **Async MongoDB** access with Motor
- 📚 Auto-generated Swagger docs

## 🧠 How resume generation works
```
Job description ──┐
Personal details ─┼──► prompt builder ──► Ollama (local LLM) ──► tailored resume ──► .docx
Work history ─────┘          (MongoDB)
```
Running the model locally keeps personal data on your own machine.

## 🔌 API overview
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/auth/register` | Create an account |
| `POST` | `/api/v1/auth/login` | Get a JWT access token |
| `GET` | `/api/v1/auth/users/me` | Current user |
| `POST` | `/api/v1/auth/personal_details/` | Save personal details |
| `POST` | `/api/v1/auth/work_history/` | Add work history |
| `POST` | `/api/v1/company/create_resume/{user_id}` | Generate a resume for a job description |

## 📁 Project structure
```
backend/
├── main.py                    # App factory, startup events, routers
├── app/api/v1/endpoints/      # auth, company, job_application, resume
├── core/                      # config, security (JWT/hashing), auth, migrations
├── db/                        # MongoDB connection
├── models/                    # Pydantic models
└── utils/                     # resume generator, helpers, auto-increment IDs
```

## 🚀 Getting started
**Prerequisites:** Python 3.10+, MongoDB, and [Ollama](https://ollama.com) with a model pulled (`ollama pull orca-mini`).
```bash
git clone https://github.com/fagami1423/job_tracker.git
cd job_tracker/backend
pip install -r requirements.txt
```
Create `backend/.env`:
```
SECRET_KEY=generate-a-long-random-string
MONGO_DETAILS=mongodb://localhost:27017
```
Run the API:
```bash
uvicorn main:app --reload
```
Docs are at http://127.0.0.1:8000/docs.

## 🛣️ Roadmap
- [ ] React frontend dashboard
- [ ] Application status pipeline (applied → interview → offer)
- [ ] Docker Compose (API + MongoDB + Ollama)
- [ ] Test suite and CI

## 👤 Author
**Raj Kumar Phagami**: [GitHub](https://github.com/fagami1423)
