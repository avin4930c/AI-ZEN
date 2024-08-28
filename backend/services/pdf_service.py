import os
from fastapi.responses import JSONResponse


async def handle_upload_pdf(file, pdf_text_storage, extract_text_from_pdf):
    try:
        os.makedirs("pdfs", exist_ok=True)

        file_path = f"pdfs/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        extracted_text = extract_text_from_pdf(file_path)

        if not extracted_text:
            return JSONResponse(status_code=400, content={"detail": "Failed to extract text from the PDF. The file might be empty or not readable."})

        pdf_text_storage[file.filename] = extracted_text

        return JSONResponse(content={"filename": file.filename, "message": "PDF uploaded and text extracted successfully."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": f"Error processing PDF: {str(e)}"})
