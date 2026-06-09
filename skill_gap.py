import pandas as pd

def find_missing_skills(resume_text, job_description):

    skills_df = pd.read_csv("data/skills.csv")

    skills = skills_df["skill"].tolist()

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_skills = []
    job_skills = []

    for skill in skills:

        if skill in resume_text:
            resume_skills.append(skill)

        if skill in job_description:
            job_skills.append(skill)

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    return sorted(missing_skills)