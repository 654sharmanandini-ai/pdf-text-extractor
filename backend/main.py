from fastapi import FastAPI, UploadFile, File
import shutil
import os
from extractor import extract_all_text

app = FastAPI()

@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_all_text(temp_file)
    os.remove(temp_file)

    return {"extracted_text": extracted_text}
