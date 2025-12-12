def query_prompt(resume_text, job_description): 
    prompt = f"""
            You are an ATS (Applicant Tracking System) expert.
            Analyze the following candidate resume for the job description.

            ### RESUME: {resume_text} 
            ### JOB DESCRIPTION: {job_description}

            Provide:
            1. ATS Score (0-100) 
            2. Key Strengths
            3. Missing Skills
            4. Final Recommendation (Hire / Interview / Reject)

            Format the answer clearly.
            """
    return prompt  
