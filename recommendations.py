def generate_recommendations(
    score,
    missing_skills
):

    recommendations = []

    if score < 80:
        recommendations.append(
            "Add more projects to strengthen your resume."
        )

    if missing_skills:

        recommendations.append(
            f"Learn: {', '.join(missing_skills)}"
        )

    recommendations.append(
        "Include measurable achievements in projects."
    )

    recommendations.append(
        "Keep resume length between 1-2 pages."
    )

    recommendations.append(
        "Use ATS-friendly keywords."
    )

    return recommendations