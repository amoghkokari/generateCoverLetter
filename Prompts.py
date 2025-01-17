
def build_prompt_for_google(resume, cover_letter_template, job_description):

    prompt = f'''
        RESUME :-
        {resume}

        COVER LETTER TEMPLATE :-
        {cover_letter_template}

        JOB DESCRIPTION :-
        {job_description}
        
        Can you please create an cover letter as per 'COVER LETTER TEMPLATE' based on 'RESUME' for the job based on 'JOB DESCRIPTION'
        '''
    return prompt