import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📈 Analytics Dashboard")

# --------------------------
# LOAD DATA
# --------------------------

@st.cache_data
def load_data():
    return pd.read_csv("Actual_Data.csv")

df = load_data()

# --------------------------
# CORRELATION HEATMAP
# --------------------------

st.subheader("Correlation Analysis")

numeric = df.select_dtypes(include=["int64","float64"])

corr = numeric.corr().round(2)

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    annotation_text=corr.values,
    colorscale="Viridis",
    showscale=True
)

st.plotly_chart(fig, use_container_width=True)

st.info(
"""
The heatmap shows the strength and direction of relationships
between numerical variables. Strong positive correlations indicate
variables that increase together, while negative correlations
indicate inverse relationships.
"""
)

st.divider()

# --------------------------
# DISTRIBUTION ANALYSIS
# --------------------------

st.subheader("Distribution Analysis")

left, right = st.columns(2)

with left:

    fig = px.box(
        df,
        y="Engagement_Score",
        title="Engagement Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.box(
        df,
        y="Lead_Score",
        title="Lead Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------
# SCATTER PLOT
# --------------------------

st.subheader("Lead Score vs Engagement")

fig = px.scatter(
    df,
    x="Lead_Score",
    y="Engagement_Score",
    color="High_Engagement",
    title="Lead Score vs Engagement"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------
# BUSINESS INSIGHTS
# --------------------------

st.subheader("Statistical Findings")

c1,c2=st.columns(2)

with c1:

    st.success("""
### ANOVA

✔ Pitch Category

F = 216.30

p < 0.001

Significant
""")

    st.success("""
### Script Tone

F = 147.88

p < 0
