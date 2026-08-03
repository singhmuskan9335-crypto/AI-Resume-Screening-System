import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def show_ats_gauge(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#fff4cc"},
                    {"range": [70, 100], "color": "#ccffcc"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True,
        key=f"gauge_{score}"
    )

def show_skill_pie(matched_skills, missing_skills):

    labels = ["Matched Skills", "Missing Skills"]

    values = [len(matched_skills), len(missing_skills)]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.5,
        title="Skills Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key=f"skill_pie_{len(matched_skills)}_{len(missing_skills)}"
    )


def show_skill_bar(skills):

    if len(skills) == 0:
        return

    fig = px.bar(
        x=skills,
        y=[1] * len(skills),
        title="Skills Found",
        labels={
            "x": "Skills",
            "y": "Presence"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key=f"skill_bar_{len(skills)}"
    )