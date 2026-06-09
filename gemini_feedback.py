import google.generativeai as genai

genai.configure(
    
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def get_resume_feedback(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Analyze the following resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

ATS Analysis

Strengths

Weaknesses

Missing Skills

Interview Readiness

Recommendations

Use bullet points.
Keep the response concise and professional.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"