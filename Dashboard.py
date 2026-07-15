import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Outreach Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv("Actual_Data_Final.csv")

df = load_data()

# -----------------------------
# KPI CARDS
# -----------------------------

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
    "Average Conversion Probability",
    round(df["Conversion_Probability"].mean(),2)
)

st.markdown("---")

# -----------------------------
# ROW 1
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="Engagement_Score",
        nbins=30,
        title="Engagement Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.histogram(
        df,
        x="Lead_Score",
        nbins=30,
        title="Lead Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROW 2
# -----------------------------

st.markdown("---")

col1, col2 = st.columns(2)

course = (
    df.groupby("Course")["Engagement_Score"]
    .mean()
    .reset_index()
)

fig = px.bar(
    course,
    x="Course",
    y="Engagement_Score",
    title="Average Engagement by Course",
    color="Engagement_Score"
)

col1.plotly_chart(fig, use_container_width=True)

region = (
    df.groupby("Region")["Engagement_Score"]
    .mean()
    .reset_index()
)

fig = px.bar(
    region,
    x="Region",
    y="Engagement_Score",
    title="Average Engagement by Region",
    color="Engagement_Score"
)

col2.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROW 3
# -----------------------------

st.markdown("---")

fig = px.box(
    df,
    x="Followup_Gap",
    y="Engagement_Score",
    color="Followup_Gap",
    title="Follow-up Gap vs Engagement"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# HIGH ENGAGEMENT
# -----------------------------

st.markdown("---")

engagement = (
    df["High_Engagement"]
    .value_counts()
    .reset_index()
)

engagement.columns = [
    "High_Engagement",
    "Count"
]

fig = px.pie(
    engagement,
    names="High_Engagement",
    values="Count",
    title="High Engagement Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# DATA PREVIEW
# -----------------------------

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)
