from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load Model Once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def calculate_match_score(
    resume_text,
    job_description
):

    # ---------------------------
    # Semantic Similarity
    # ---------------------------

    resume_embedding = model.encode(
        resume_text
    )

    job_embedding = model.encode(
        job_description
    )

    semantic_score = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    semantic_score *= 100

    # ---------------------------
    # Skill Overlap
    # ---------------------------

    skills_df = pd.read_csv(
        "data/skills.csv"
    )

    skills = skills_df["skill"].tolist()

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_skills = set()
    job_skills = set()

    for skill in skills:

        if skill in resume_text:
            resume_skills.add(skill)

        if skill in job_description:
            job_skills.add(skill)

    if len(job_skills) > 0:

        overlap_score = (
            len(
                resume_skills.intersection(
                    job_skills
                )
            )
            /
            len(job_skills)
        ) * 100

    else:
        overlap_score = 50

    # ---------------------------
    # Final Weighted Score
    # ---------------------------

    final_score = (
        semantic_score * 0.6
        +
        overlap_score * 0.4
    )

    return round(
        min(final_score, 100),
        2
    )