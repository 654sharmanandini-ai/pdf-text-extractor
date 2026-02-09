import streamlit as st
import requests

st.title("📄 PDF Text & Image Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    files = {"file": uploaded_file}
    response = requests.post("http://backend:8000/extract", files=files)

    if response.status_code == 200:
        st.text_area(
            "Extracted Text",
            response.json()["extracted_text"],
            height=400
        )
    else:
        st.error("Failed to extract text")
