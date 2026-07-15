import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Statistical Analytics")

# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv("Actual_Data_Final.csv")

df = load_data()

# -----------------------------
# CORRELATION HEATMAP
# -----------------------------

st.subheader("Correlation Analysis")

numeric = df.select_dtypes(include=["int64", "float64"])

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

st.info("""
The correlation heatmap illustrates relationships among numerical variables.
Higher positive values indicate stronger positive associations, while negative values indicate inverse relationships.
""")

st.divider()

# -----------------------------
# DISTRIBUTION ANALYSIS
# -----------------------------

st.subheader("Distribution Analysis")

c1, c2 = st.columns(2)

with c1:

    fig = px.box(
        df,
        y="Engagement_Score",
        title="Engagement Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:

    fig = px.box(
        df,
        y="Lead_Score",
        title="Lead Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# SCATTER PLOT
# -----------------------------

st.subheader("Lead Score vs Engagement")

fig = px.scatter(
    df,
    x="Lead_Score",
    y="Engagement_Score",
    color="High_Engagement",
    hover_data=["Course", "Region"],
    title="Relationship between Lead Score and Engagement"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# SUMMARY STATISTICS
# -----------------------------

st.subheader("Summary Statistics")

st.dataframe(
    df.describe().round(2),
    use_container_width=True
)

st.divider()

# -----------------------------
# STATISTICAL TESTS
# -----------------------------

st.subheader("Statistical Test Summary")

left, right = st.columns(2)

with left:

    st.success("""
### ANOVA Results

✔ Pitch Category

F = 216.30

p < 0.001

------------------------

✔ Script Tone

F = 147.88

p < 0.001

------------------------

✔ Follow-up Gap

F = 234.62

p < 0.001
""")

with right:

    st.success("""
### Additional Tests

✔ Regional Reachability

F = 58.49

p < 0.001

------------------------

✔ Chi-Square Test

χ² = 44.19

p < 0.001

------------------------

✔ Independent T-Test

t = 0.556

p = 0.578
""")

st.divider()

# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------

st.subheader("Business Insights")

st.markdown("""
### Key Findings

- Follow-Up Gap was the strongest factor affecting learner engagement.

- Pitch Category significantly influenced learner responses.

- Script Tone demonstrated a statistically significant impact.

- Regional Reachability affected learner engagement.

- Learners with higher Lead Scores generally showed higher Engagement Scores.

- Most statistical tests supported the research hypotheses.
""")

st.divider()

# -----------------------------
# PROJECT METRICS
# -----------------------------

st.subheader("Project Summary")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Learner Records", "5,000+")

m2.metric("Hypotheses Tested", "6")

m3.metric("Significant Results", "5")

m4.metric("Automation Efficiency", "66.7%")
