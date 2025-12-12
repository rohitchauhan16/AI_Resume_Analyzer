from pypdf import PdfReader

def extract_pdf(uploaded_file): 
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    
    except Exception as e:
        return f"Error reading PDF: {e}"
