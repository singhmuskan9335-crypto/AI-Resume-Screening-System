from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    score,
    rating,
    matched_skills,
    missing_skills,
    suggestions
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Resume Screening Report</b>", styles["Heading1"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["BodyText"]))

    story.append(Paragraph(f"<b>Resume Rating:</b> {rating}", styles["BodyText"]))

    story.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<b>AI Suggestions</b>", styles["Heading2"]))

    for suggestion in suggestions:
        story.append(Paragraph(f"• {suggestion}", styles["BodyText"]))

    pdf.build(story)