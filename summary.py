def generate_summary(score, matched_skills, missing_skills):

    summary = f"""
Candidate Summary

Overall ATS Score : {score}%

Strong Skills:
"""

    if matched_skills:
        for skill in matched_skills:
            summary += f"\n✔ {skill}"
    else:
        summary += "\nNo matched skills found."

    summary += "\n\nAreas to Improve:\n"

    if missing_skills:
        for skill in missing_skills:
            summary += f"\n❌ {skill}"
    else:
        summary += "\nNo missing skills."

    if score >= 90:
        recommendation = "Hire Immediately"

    elif score >= 75:
        recommendation = "Shortlist for Interview"

    elif score >= 60:
        recommendation = "Needs Technical Evaluation"

    else:
        recommendation = "Needs Skill Improvement"

    summary += f"\n\nRecommendation:\n{recommendation}"

    return summary