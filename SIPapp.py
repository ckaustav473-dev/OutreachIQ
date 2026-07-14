import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="OutreachIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.big-font{
    font-size:38px;
    font-weight:bold;
    color:#1F4E79;
}

.sub-font{
    font-size:20px;
    color:#444444;
}

.metric-card{
    background:#FFFFFF;
    padding:15px;
    border-radius:12px;
    box-shadow:2px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("📊 OutreachIQ")

st.sidebar.markdown("---")

st.sidebar.info(
"""
**MBA Business Analytics Project**

TechnGlobal Private Limited

Summer Internship
"""
)

st.sidebar.markdown("---")

st.sidebar.success(
"""
Navigate using the pages on the left.

Dashboard

Analytics

Prediction

Segmentation

Automation

About
"""
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
"<p class='big-font'>OutreachIQ</p>",
unsafe_allow_html=True
)

st.markdown(
"<p class='sub-font'>AI-Powered Outreach Analytics Platform</p>",
unsafe_allow_html=True
)

st.write("")

st.markdown("---")

# -----------------------------
# PROJECT DESCRIPTION
# -----------------------------

st.markdown("## Project Overview")

st.write("""
OutreachIQ is an end-to-end Business Analytics platform developed
during the Summer Internship at **TechnGlobal Private Limited**.

The platform combines:

- CRM Analytics
- Outreach Automation
- Business Intelligence
- Statistical Analysis
- Machine Learning
- Learner Segmentation

to improve learner engagement and outreach efficiency.
""")

st.markdown("---")

# -----------------------------
# KPI SECTION
# -----------------------------

st.markdown("## Key Business Outcomes")

col1,col2,col3,col4=st.columns(4)

with col1:

    st.metric(
        "Learner Records",
        "5,000+"
    )

with col2:

    st.metric(
        "Execution Time Reduction",
        "66.7%"
    )

with col3:

    st.metric(
        "Productivity Increase",
        "60%"
    )

with col4:

    st.metric(
        "Statistical Tests",
        "6"
    )

st.markdown("---")

# -----------------------------
# FEATURES
# -----------------------------

st.markdown("## Application Modules")

c1,c2=st.columns(2)

with c1:

    st.success("""
📊 Dashboard

Interactive KPIs and charts
""")

    st.success("""
📈 Analytics

EDA, Heatmaps, ANOVA,
Chi-Square and T-Test
""")

    st.success("""
🤖 Prediction

Predict High Engagement
using Machine Learning
""")

with c2:

    st.success("""
👥 Segmentation

K-Means Learner Clustering
""")

    st.success("""
📩 Automation

Outreach Workflow
""")

    st.success("""
📋 Recommendations

Business Insights
""")

st.markdown("---")

# -----------------------------
# BUSINESS IMPACT
# -----------------------------

st.markdown("## Business Impact")

st.write("""

This application demonstrates how Business Analytics can be
combined with CRM automation to improve outreach management.

Major outcomes include:

✔ Reduced outreach execution time by **66.7%**

✔ Increased outreach productivity by **60%**

✔ Analyzed **5,000+ learner records**

✔ Identified statistically significant engagement factors

✔ Developed predictive models for learner engagement

✔ Segmented learners for targeted outreach strategies

""")

st.markdown("---")

st.caption(
"Developed by Kaustav Chakraborty | MBA Business Analytics | SIBM Bengaluru"
)
