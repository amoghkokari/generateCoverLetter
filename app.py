"""
Main file contains execution flow to the entire process
"""

import streamlit as st
from AIModels import getAI

def main():

    st.title("AI-Powered Cover Letter Generator")
    st.write("Made with ❤️ by Amogh Mahadev kokari ©️ 2025 _||_ [linkedin](https://www.linkedin.com/in/amoghkokari/) _||_ [Portfolio](https://amoghkokari.github.io/portfolio.pdf) _||_ [Github](https://github.com/amoghkokari)")
    
    model_link = {
        "Google Gemini": "https://makersuite.google.com/app/apikey",
        "Gorq": "https://console.groq.com/keys"
    }

    # AI Model Selection
    st.write("OpenAI GPT-3 coming soon !")
    ai_model = st.selectbox("Select AI Model", ["Google Gemini", "Gorq"])

    st.link_button("Click for API KEY (select create api key in new project)", model_link[ai_model], type="secondary")
    
    # API Key Input
    api_key = st.text_input(f"Enter {ai_model} API Key", type="password")
    
    # Resume Input
    resume = st.text_area("Paste Your Resume")
    
    # Cover Letter Template Input
    cover_letter_template = st.text_area("Paste Cover Letter Template")
    
    # Job Description Input
    job_description = st.text_area("Paste Job Description")
    
    # Generate Button
    if st.button("Generate Cover Letter"):
        if not resume or not cover_letter_template or not job_description:
            st.error("Please fill in all fields before generating the cover letter.")
        else:
            try:
                generated_cover_letter = getAI(ai_model, api_key, resume, cover_letter_template, job_description)

                st.subheader("Generated Cover Letter")
                st.text_area("response", generated_cover_letter,label_visibility="hidden", height=400)

            except Exception as error:
                st.write("Please check your Api key, probable issue", SystemExit(error))
    
    st.write("Made with ❤️ by Amogh Mahadev kokari ©️ 2025 _||_ [linkedin](https://www.linkedin.com/in/amoghkokari/) _||_ [Portfolio](https://amoghkokari.github.io/portfolio.pdf) _||_ [Github](https://github.com/amoghkokari)")

if __name__ == "__main__":
    main()
