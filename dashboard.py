import streamlit as st


def show_dashboard(score, resume_skills, missing_skills):

    matched = len(resume_skills) - len(missing_skills)

    st.subheader("📊 Recruiter Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🎯 ATS Score",
            f"{score}%"
        )

    with col2:
        if score >= 90:
            rating = "Excellent"
        elif score >= 75:
            rating = "Very Good"
        elif score >= 60:
            rating = "Good"
        else:
            rating = "Needs Improvement"

        st.metric(
            "⭐ Resume Rating",
            rating
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "✅ Matched Skills",
            matched
        )

    with col4:
        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )

    st.divider()