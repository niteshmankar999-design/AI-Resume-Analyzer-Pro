import pandas as pd

def keyword_analysis(
    resume_text,
    job_description
):

    skills_df = pd.read_csv(
        "data/skills.csv"
    )

    skills = skills_df["skill"].tolist()

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched_keywords = []
    missing_keywords = []

    for skill in skills:

        if skill in job_description:

            if skill in resume_text:
                matched_keywords.append(
                    skill
                )

            else:
                missing_keywords.append(
                    skill
                )

    total_keywords = (
        len(matched_keywords)
        +
        len(missing_keywords)
    )

    if total_keywords > 0:

        coverage = round(
            (
                len(matched_keywords)
                /
                total_keywords
            ) * 100,
            2
        )

    else:
        coverage = 0

    return (
        matched_keywords,
        missing_keywords,
        coverage
    )