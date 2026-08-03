import pandas as pd
import streamlit as st


def show_candidate_ranking(candidates):

    if not candidates:
        return

    df = pd.DataFrame(candidates)

    df = df.sort_values(
        by="ATS Score",
        ascending=False
    )

    df.insert(0, "Rank", range(1, len(df) + 1))

    st.subheader("🏆 Candidate Ranking")

    st.dataframe(
        df,
        use_container_width=True
    )