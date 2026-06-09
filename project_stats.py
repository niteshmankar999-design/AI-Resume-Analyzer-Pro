def get_project_stats(skills, score, match_score):

    return {
        "skills_count": len(skills),
        "ats_score": score,
        "job_match": match_score if match_score else 0
    }