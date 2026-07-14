import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# PAGE CONFIG
# --------------------------

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Outreach Dashboard")

# --------------------------
# LOAD DATA
# --------------------------

@st.cache_data
def load_data():
    return pd.read_csv("Actual_Data.csv")

df = load_data()

# --------------------------
# KPI CARDS
# --------------------------

st.subheader("Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Learners",
    len(df)
)

c2.metric(
    "Average Engagement",
    round(df["Engagement_Score"].mean(),2)
)

c3.metric(
    "Average Lead Score",
    round(df["Lead_Score"].mean(),2)
)

c4.metric(
    "Average Conversion %",
    round(df["Conversion_Probability"].mean(),2)
)

st.divider()

# --------------------------
# ROW 1
# --------------------------

left,right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="Engagement_Score",
        nbins=20,
        title="Engagement Score Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    fig = px.histogram(
        df,
        x="Lead_Score",
        nbins=20,
        title="Lead Score Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

st.divider()

# --------------------------
# COURSE ANALYSIS
# --------------------------

left,right = st.columns(2)

course = (
    df.groupby("Course")["Engagement_Score
