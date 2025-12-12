from huggingface_hub import InferenceClient
from prompts import query_prompt

HF_API_KEY = "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"
client = InferenceClient(api_key=HF_API_KEY) 

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"   # Free & stable model 
# MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"   # Free & stable model  

def generate_response(resume_text, job_description):  
    prompt = query_prompt(resume_text, job_description)  

    response = client.chat_completion(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.3
    )

    return response.choices[0].message["content"]

