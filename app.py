import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions

from components.dashboard import show_dashboard
from components.analysis import analyze_resume
from components.charts import show_ats_gauge, show_skill_pie
from pathlib import Path
from utils.candidate_ranker import rank_candidates
import pandas as pd
from utils.excel_export import export_to_excel

from database.database import (
    create_database,
    get_all_candidates,
    search_candidate,
    filter_candidates,
    get_dashboard_stats,
    delete_candidate
)

from database.database import (
    create_database,
    insert_candidate
)

def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"

    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.error(f"CSS file not found: {css_file}")


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)
create_database()
load_css()



# ==============================
# Sidebar
# ==============================

st.sidebar.title("🤖 AI Resume Screening")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Resume Analysis",
        "🏆 Candidate Ranking",
        "📊 Reports",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Developed using Python, Streamlit and NLP"
)

# -----------------------------
# Title
# -----------------------------
if menu == "🏠 Home":
    st.title("🤖 AI Resume Screening & Candidate Ranking System")

    st.caption(
        "Industry-Level Recruitment Assistant powered by Python, NLP and Machine Learning"
    )

    st.markdown("""
        Welcome to the **AI Resume Screening System**.

    This application helps recruiters analyze resumes, compare them with job descriptions, calculate ATS scores, detect missing skills, and rank candidates automatically.

    ### Features

    ✅ Resume Parsing

    ✅ ATS Score Calculation

    ✅ Skill Matching

    ✅ Missing Skill Detection

    ✅ AI Resume Suggestions

    ✅ Candidate Ranking

    ✅ Professional Reports
    """)

st.divider()
if menu == "📄 Resume Analysis":
    candidate_list = []

    st.header("📄 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        resumes = st.file_uploader(
            "📄 Upload Resume(s)",
            type=["pdf", "docx"],
            accept_multiple_files=True
        )

    with col2:
        jd = st.file_uploader(
            "📋 Upload Job Description",
            type=["pdf", "txt"]
        )

    st.divider()

    if st.button("🚀 Analyze Resume", use_container_width=True):

        if not resumes:
            st.error("Please upload at least one Resume.")

        elif jd is None:
            st.error("Please upload a Job Description.")

        else:

            for resume in resumes:

                candidate = analyze_resume(
                    resume,
                    jd
                )

                if candidate is not None:
                    candidate_list.append(candidate)

           
            
                     # Rank candidates
                    if candidate_list:
                        candidate_list = rank_candidates(candidate_list)
                        excel_file = "Candidate_Ranking.xlsx"
                        export_to_excel(
                            candidate_list,
                            excel_file
                        )
                        ranking_data = []
                        rank = 1
                        for candidate in candidate_list:
                            ranking_data.append(
                                {
                                    "Rank": rank,
                                    "Candidate": candidate["name"],
                                    "ATS Score": f"{candidate['score']}%",
                                    "Rating": candidate["rating"]
                                }
                            )

                            rank += 1

                        df = pd.DataFrame(ranking_data)
                        st.header("🏆 Candidate Ranking")
                        st.dataframe(
                            df,
                            width="stretch",
                            hide_index=True
                        )

                        with open(excel_file, "rb") as file:

                            st.download_button(
                                label="📥 Download Candidate Ranking (Excel)",
                                data=file,
                                file_name="Candidate_Ranking.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )

elif menu == "🏆 Candidate Ranking":

    st.header("🏆 Candidate Ranking")

    st.info(
        "Analyze multiple resumes from the Resume Analysis page to see the ranking."
    )

elif menu == "📊 Reports":

    st.header("📊 Candidate Reports")

    stats = get_dashboard_stats()

    total_candidates = stats[0]

    average_score = round(stats[1], 2) if stats[1] else 0

    highest_score = stats[2] if stats[2] else 0

    lowest_score = stats[3] if stats[3] else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Total Candidates",
            total_candidates
        )

    with col2:
        st.metric(
            "📈 Average ATS",
            average_score
        )

    with col3:
        st.metric(
            "🏆 Highest ATS",
            highest_score
        )

    with col4:
        st.metric(
            "📉 Lowest ATS",
            lowest_score
        )

    st.divider()

    rating_filter = st.selectbox(
        "⭐ Filter by Rating",
        [
            "All",
            "Excellent",
            "Very Good",
            "Good",
            "Average",
            "Poor"
        ]
    )

    search_name = st.text_input(
        "🔍 Search Candidate"
    )

    if search_name:

        candidates = search_candidate(search_name)

    elif rating_filter != "All":

        candidates = filter_candidates(rating_filter)

    else:

        candidates = get_all_candidates()

    if len(candidates) == 0:

        st.warning("No candidates found in the database.")

    else:

        report_data = []

        rank = 1

        for candidate in candidates:

            report_data.append(
                {
                    "Rank": rank,
                    "Candidate": candidate[0],
                    "ATS Score": candidate[1],
                    "Rating": candidate[2]
                }
            )

            rank += 1

        df = pd.DataFrame(report_data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("🗑 Delete Candidate")

        candidate_names = [candidate[0] for candidate in candidates]

        selected_candidate = st.selectbox(
            "Select Candidate",
            candidate_names
        )

        if st.button("🗑 Delete Candidate"):

            delete_candidate(selected_candidate)

            st.success("Candidate deleted successfully!")

            st.rerun()

elif menu == "ℹ About":

    st.header("ℹ About")

    st.markdown("""
### AI Resume Screening System

This project helps recruiters:

- 📄 Analyze resumes
- 🎯 Match resumes with Job Descriptions
- 📊 Calculate ATS Score
- 🧠 Detect Missing Skills
- 💡 Generate AI Suggestions
- 🏆 Rank Candidates
- 📁 Export Excel Reports
- 🗄 Store Candidate Data using SQLite

**Developed by:** Himanshu Singh
""")
st.divider()

st.caption(
    "© 2026 AI Resume Screening & Candidate Ranking System | Version 1.0 | Developed by Himanshu Singh"
)


    


                                  
                                                                                        
                                                               
                               