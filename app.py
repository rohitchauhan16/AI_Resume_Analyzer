import streamlit as st
from utils import extract_pdf
from generator import generate_response 


st.set_page_config(page_title="ATS Resume Analyzer", layout="centered") 

st.title("📄 ATS Resume Analyzer") 
st.write("Upload your resume (PDF) and paste the job description.")

uploaded_pdf = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=180)

if st.button("Analyze Resume"):
    if not uploaded_pdf:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        with st.spinner("Reading PDF..."):
            resume_text = extract_pdf(uploaded_pdf) 

        with st.spinner("Analyzing with AI..."):
            report = generate_response(resume_text, job_description)  

        st.subheader("📊 ATS Report")
        st.write(report)
