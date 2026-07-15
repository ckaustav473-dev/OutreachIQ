import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Automation",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Outreach Automation")

st.write("""
This module demonstrates the automation framework developed during
the Summer Internship at **TechnGlobal Private Limited** to improve
learner outreach efficiency.
""")

st.markdown("---")

# ---------------------------------
# KPI CARDS
# ---------------------------------

st.subheader("Automation Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Execution Time",
    "5 sec",
    "-66.7%"
)

c2.metric(
    "Productivity",
    "40 Leads/hr",
    "+60%"
)

c3.metric(
    "Manual Errors",
    "0%",
    "-100%"
)

c4.metric(
    "Workflow",
    "Automated"
)

st.markdown("---")

# ---------------------------------
# COMPARISON TABLE
# ---------------------------------

st.subheader("Manual vs Automated Process")

comparison = pd.DataFrame({

    "Metric":[
        "Execution Time",
        "Leads Processed / Hour",
        "Manual Errors",
        "Follow-up Consistency",
        "Scalability"
    ],

    "Manual":[
        "15 sec",
        "25",
        "1-2%",
        "Moderate",
        "Limited"
    ],

    "Automated":[
        "5 sec",
        "40",
        "0%",
        "High",
        "Excellent"
    ]

})

st.dataframe(
    comparison,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# BAR CHART
# ---------------------------------

chart = pd.DataFrame({

    "Process":[
        "Manual",
        "Automated"
    ],

    "Execution Time":[
        15,
        5
    ]

})

fig = px.bar(
    chart,
    x="Process",
    y="Execution Time",
    color="Process",
    title="Execution Time Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# PRODUCTIVITY
# ---------------------------------

productivity = pd.DataFrame({

    "Process":[
        "Manual",
        "Automated"
    ],

    "Leads per Hour":[
        25,
        40
    ]

})

fig = px.bar(
    productivity,
    x="Process",
    y="Leads per Hour",
    color="Process",
    title="Outreach Productivity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# WORKFLOW
# ---------------------------------

st.subheader("Automated Outreach Workflow")

st.info("""

Lead Generation

⬇

CRM Data Collection

⬇

Automated WhatsApp Outreach

⬇

Follow-up Scheduling

⬇

Learner Engagement Tracking

⬇

Lead Scoring

⬇

Business Intelligence Dashboard

⬇

Decision Support

""")

st.markdown("---")

# ---------------------------------
# BUSINESS BENEFITS
# ---------------------------------

st.subheader("Business Benefits")

st.success("""

✔ Reduced execution time by **66.7%**

✔ Increased outreach productivity by **60%**

✔ Eliminated manual processing errors

✔ Improved follow-up consistency

✔ Enabled scalable outreach

✔ Supported data-driven decision making

✔ Improved learner engagement

✔ Optimized resource utilization

""")

st.markdown("---")

# ---------------------------------
# INTERNSHIP HIGHLIGHTS
# ---------------------------------

st.subheader("Internship Outcomes")

st.write("""

During the internship, an automation framework was developed
to streamline learner outreach operations.

The system integrated CRM concepts, WhatsApp automation,
Business Intelligence, statistical analysis, and machine
learning to improve outreach effectiveness and operational
efficiency.

The automation framework reduced repetitive manual work,
improved follow-up consistency, and enabled data-driven
decision making through real-time analytical insights.

""")
