# Setup

## Clone
git clone …

## Virtual environment
python3 -m venv .venv
.\.venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Install Tesseract 
Download from https://github.com/UB-Mannheim/tesseract/wiki

## Run backend
uvicorn backend.main:app --reload

## Run frontend
streamlit run frontend/app.py
