import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions
from utils.rating import get_resume_rating
from utils.strength import get_strengths
from utils.weakness import get_weaknesses
from utils.summary import generate_summary

from utils.report_generator import generate_pdf_report
from utils.semantic_match import calculate_semantic_similarity
from database.database import insert_candidate


from components.dashboard import show_dashboard
from components.charts import (
    show_ats_gauge,
    show_skill_pie,
    show_skill_bar
)

def analyze_resume(resume, jd):

    if resume is None:
        st.error("Please upload a Resume.")
        return

    if jd is None:
        st.warning("Please upload a Job Description.")
        return

    # Extract Resume
    resume_text = extract_text_from_pdf(resume)

    # Extract Job Description
    jd_text = extract_text_from_pdf(jd)

    semantic_score = calculate_semantic_similarity(
        resume_text,
        jd_text
    )

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(jd_text)

    # Calculate ATS Score
    score, matched_skills, missing_skills = calculate_ats_score(
        resume_skills,
        job_skills
    )

    st.subheader("🤖 AI Semantic Match")

    st.success(f"{semantic_score}% Match")

    # Dashboard
    show_dashboard(
        score,
        resume_skills,
        missing_skills
    )

    rating = get_resume_rating(score)

    st.subheader("🏅 Resume Rating")

    st.success(rating)

    st.divider()

    show_ats_gauge(score)

    show_skill_pie(
        matched_skills,
        missing_skills
    )

    st.divider()

    # Matched Skills
    st.subheader("✅ Matched Skills")

    for skill in matched_skills:
        st.success(skill)
    strengths = get_strengths(matched_skills)

    st.subheader("💪 Candidate Strengths")

    for skill in strengths:
        st.success(f"✔ {skill}")

    # Missing Skills
    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.error(skill)
    weaknesses = get_weaknesses(missing_skills)

    st.subheader("⚠ Areas to Improve")

    for skill in weaknesses:
        st.warning(f"❌ {skill}")

    # Suggestions
    suggestions = generate_suggestions(missing_skills)

    st.subheader("💡 AI Suggestions")

    for suggestion in suggestions:
        st.info(suggestion)

    summary = generate_summary(
        score,
        matched_skills,
        missing_skills
    )

    st.subheader("👤 Candidate Summary")

    st.info(summary)

    # Resume Text
    with st.expander("📄 Resume Preview"):

        st.text_area(
            "Resume",
            resume_text,
            height=350
        )

    report_file = "Candidate_Report.pdf"

    generate_pdf_report(
        report_file,
        score,
        rating,
        matched_skills,
        missing_skills,
        suggestions
    )

    with open(report_file, "rb") as file:
        st.download_button(
            "📥 Download Candidate Report",
            data=file,
            file_name="Candidate_Report.pdf",
            mime="application/pdf"
        )

        insert_candidate(
            resume.name,
            score,
            rating
        )

        candidate_name = resume.name.replace(".pdf", "").replace(".docx", "")

        return {
            "name": candidate_name,
            "score": score,
            "rating": rating
        }