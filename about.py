import streamlit as st

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("---")

# ---------------------------------
# PROJECT OVERVIEW
# ---------------------------------

st.header("Project Overview")

st.write("""
**OutreachIQ** is an AI-powered Business Analytics platform developed
during the Summer Internship at **TechnGlobal Private Limited**.

The project aims to improve learner outreach by integrating
CRM concepts, Business Intelligence, Automation,
Statistical Analysis, and Machine Learning.

The platform enables organizations to identify highly engaged
learners, prioritize leads, automate outreach workflows,
and make data-driven decisions.
""")

st.markdown("---")

# ---------------------------------
# OBJECTIVES
# ---------------------------------

st.header("Project Objectives")

st.markdown("""

- Improve learner engagement through data analytics

- Identify factors affecting learner conversion

- Predict High Engagement learners

- Segment learners for targeted outreach

- Automate repetitive outreach activities

- Improve operational efficiency

- Support business decision making

""")

st.markdown("---")

# ---------------------------------
# DATASET
# ---------------------------------

st.header("Dataset")

st.write("""

The analysis was performed on approximately **5,000 learner records**
containing outreach and engagement-related variables.

Major attributes include:

• Region

• Course

• Time Slot

• Pitch Category

• Script Tone

• Follow-up Gap

• Outreach Type

• Attempts

• Lag

• ELT

• Lead Score

• Conversion Probability

• Engagement Score

• High Engagement

""")

st.markdown("---")

# ---------------------------------
# ANALYTICS
# ---------------------------------

st.header("Analytics Performed")

st.success("""

✔ Exploratory Data Analysis

✔ Distribution Analysis

✔ Correlation Analysis

✔ ANOVA

✔ Chi-Square Test

✔ Independent Sample T-Test

✔ Logistic Regression

✔ Decision Tree Classification

✔ K-Means Clustering

""")

st.markdown("---")

# ---------------------------------
# TECHNOLOGIES
# ---------------------------------

st.header("Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:

    st.info("""

Programming Language

• Python

Libraries

• Pandas

• NumPy

• Scikit-Learn

• Plotly

• Matplotlib

""")

with tech2:

    st.info("""

Frameworks

• Streamlit

Tools

• Jupyter Notebook

• GitHub

• Streamlit Cloud

• Visual Studio Code

""")

st.markdown("---")

# ---------------------------------
# BUSINESS OUTCOMES
# ---------------------------------

st.header("Business Outcomes")

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Learner Records",
        "5,000+"
    )

    st.metric(
        "Execution Time Reduction",
        "66.7%"
    )

    st.metric(
        "Productivity Increase",
        "60%"
    )

with c2:

    st.metric(
        "Machine Learning Models",
        "3"
    )

    st.metric(
        "Statistical Tests",
        "6"
    )

    st.metric(
        "Significant Results",
        "5"
    )

st.markdown("---")

# ---------------------------------
# FUTURE SCOPE
# ---------------------------------

st.header("Future Scope")

st.write("""

Future enhancements may include:

• Real-time CRM integration

• WhatsApp Business API integration

• Random Forest and XGBoost models

• Natural Language Processing

• Live Power BI dashboards

• Automated recommendation engine

• Cloud deployment

• Real-time learner monitoring

""")

st.markdown("---")

# ---------------------------------
# AUTHOR
# ---------------------------------

st.header("Developer")

st.success("""

**Kaustav Chakraborty**

Project:

AI-Powered Outreach Analytics Platform

""")

st.markdown("---")

st.caption("© 2026 OutreachIQ")
