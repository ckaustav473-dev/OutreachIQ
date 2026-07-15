import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="Learner Segmentation",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Learner Segmentation")

st.write("""
Segment learners into clusters based on their engagement behaviour
using the trained K-Means clustering model.
""")

# ---------------------------------------
# LOAD MODELS
# ---------------------------------------

kmeans = joblib.load("kmeans.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------------------
# USER INPUT
# ---------------------------------------

col1, col2 = st.columns(2)

with col1:

    engagement = st.slider(
        "Engagement Score",
        0.0,
        100.0,
        70.0
    )

    lag = st.slider(
        "Lag",
        0.0,
        15.0,
        5.0
    )

with col2:

    attempts = st.slider(
        "Attempts",
        1,
        10,
        3
    )

# ---------------------------------------
# CLUSTER PREDICTION
# ---------------------------------------

if st.button("Generate Cluster"):

    sample = pd.DataFrame({
        "Engagement_Score":[engagement],
        "Lag":[lag],
        "Attempts":[attempts]
    })

    scaled = scaler.transform(sample)

    cluster = kmeans.predict(scaled)[0]

    st.markdown("---")

    st.success(f"Predicted Cluster : {cluster}")

    if cluster == 0:

        st.success("""
### High Value Learners

• Highly engaged

• Frequent interaction

• Highest priority

• Excellent conversion potential
""")

    elif cluster == 1:

        st.info("""
### Potential Learners

• Moderate engagement

• Regular follow-up recommended

• Good conversion opportunity
""")

    elif cluster == 2:

        st.warning("""
### Nurture Segment

• Low engagement

• Requires personalized counselling

• Increase follow-up frequency
""")

    else:

        st.error("""
### At-Risk Learners

• Very low engagement

• Intensive outreach required

• Re-engagement campaigns recommended
""")

# ---------------------------------------
# SAMPLE VISUALIZATION
# ---------------------------------------

st.markdown("---")

st.subheader("Sample Learner Position")

sample_df = pd.DataFrame({
    "Lag":[lag],
    "Engagement Score":[engagement],
    "Cluster":[str(cluster) if 'cluster' in locals() else "Not Predicted"]
})

fig = px.scatter(
    sample_df,
    x="Lag",
    y="Engagement Score",
    color="Cluster",
    size=[20],
    title="Learner Position"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# BUSINESS INTERPRETATION
# ---------------------------------------

st.markdown("---")

st.subheader("Business Insights")

st.info("""
K-Means clustering groups learners with similar engagement
behaviour into distinct segments.

Business Benefits:

• Identify high-value learners

• Personalize outreach campaigns

• Optimize counsellor allocation

• Improve follow-up prioritization

• Increase conversion opportunities
""")

# ---------------------------------------
# CLUSTER SUMMARY
# ---------------------------------------

st.markdown("---")

st.subheader("Segmentation Summary")

summary = pd.DataFrame({
    "Cluster":[0,1,2,3],
    "Description":[
        "High Value",
        "Potential",
        "Nurture",
        "At-Risk"
    ]
})

st.dataframe(summary, use_container_width=True)
