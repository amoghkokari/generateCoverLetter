import google.generativeai as genai
from Prompts import build_prompt_for_google
from streamlit import secrets
from groq import Groq

def getAI(ai_model, api_key, resume, cover_letter_template, job_description):
    
    if ai_model == "Google Gemini":
        gemini_api_key = api_key if api_key else secrets["gemini_api_key"]
        prompt = build_prompt_for_google(resume, cover_letter_template, job_description)

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel(model_name = "gemini-pro")
        model_resp = model.generate_content(prompt)

        return model_resp.text

    if ai_model == "Gorq":
        gorq_api_key = api_key if api_key else secrets["gorq_api_key"]
        client = Groq(api_key=gorq_api_key)

        prompt = build_prompt_for_google(resume, cover_letter_template, job_description)

        gorq_resp = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are Cover letter creator expert"
                },
                {
                    "role": "user",
                    "content": prompt
                }],
            model="llama-3.3-70b-versatile")
        
        return gorq_resp.choices[0].message.content
    
    return "gen AI key or some other issues"