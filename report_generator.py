from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_report(
    score,
    skills,
    match_score,
    missing_skills,
    recommendations
):

    filename = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Resume Score: {score}/100",
            styles["Normal"]
        )
    )

    if match_score is not None:
        content.append(
            Paragraph(
                f"Job Match Score: {match_score}%",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    for skill in skills:
        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:
        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for rec in recommendations:
        content.append(
            Paragraph(
                f"• {rec}",
                styles["Normal"]
            )
        )

    doc.build(content)

    return filename