from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.model import SessionLocal
import os
import google.generativeai as genai
from prompts.prompts import Prompt
from dotenv import load_dotenv

from utils.extract_text import extract_text_from_pdf
from services.chat_service import handle_chat_request
from services.pdf_service import handle_upload_pdf

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pdf_text_storage = {}

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=Prompt.get_prompt(),
)


class ChatRequest(BaseModel):
    message: str


def update_system_instruction(new_instruction):
    global model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=new_instruction,
    )


async def prompt_parser(message: str, prompt: str, prompt_type: str, data: str = None) -> str:
    update_system_instruction(prompt)

    if prompt_type == "db_analyser" and data:
        full_message = f"{message}\n\nData: {data}"
    else:
        full_message = message

    response = model.generate_content(full_message)
    result = response.text.strip()

    if prompt_type == "sql" and result.startswith("```sql"):
        result = result[6:].strip()
        if result.endswith("```"):
            result = result[:-3].strip()

    return result


@app.post("/api/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        result = await handle_upload_pdf(file, pdf_text_storage, extract_text_from_pdf)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error processing PDF: {str(e)}"})


@app.post("/api/chat")
async def generate_response(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        result = await handle_chat_request(request, pdf_text_storage, prompt_parser, db)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error processing request: {str(e)}"})
