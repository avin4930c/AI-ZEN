from fastapi import Depends
from fastapi.responses import JSONResponse
from models.model import SessionLocal
from sqlalchemy import text
from sqlalchemy.orm import Session
from prompts.prompts import Prompt, DbPrompt, DbAnalyserPrompt


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def handle_chat_request(request: str, pdf_text_storage: dict, prompt_parser, db: Session = Depends(get_db)):
    try:
        if 'pdf' in request.message.lower():
            relevant_texts = ' '.join(pdf_text_storage.values())

            if not relevant_texts:
                return JSONResponse(content={"response": "No PDF content available. Please upload a PDF file first."})
            else:
                result = await prompt_parser(
                    f"{request.message} based on the following content:\n\n{
                        relevant_texts}",
                    Prompt.get_prompt(),
                    "text"
                )
                return JSONResponse(content={"response": result})
        else:
            sql_query = await prompt_parser(request.message, DbPrompt.get_prompt(), "sql")

            valid_sql_commands = ("SELECT", "INSERT", "UPDATE", "DELETE")
            if not any(str(sql_query).upper().startswith(cmd) for cmd in valid_sql_commands):
                return JSONResponse(status_code=200, content={"response": "Please ask about the PDF content or ask about the survey data"})

            if not sql_query:
                return JSONResponse(status_code=200, content={"response": "Enough information is not available related to this."})

            try:
                result = db.execute(text(sql_query))
                results = result.fetchall()

                formatted_results = [dict(zip(result.keys(), row))
                                     for row in results]
                results_text = str(formatted_results)

                summary = await prompt_parser(request.message, DbAnalyserPrompt.get_prompt(), "db_analyser", data=results_text)
                return JSONResponse(content={"response": summary})
            except Exception as e:
                return JSONResponse(status_code=500, content={"detail": f"SQL execution error: {str(e)}"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error processing request: {str(e)}"})
