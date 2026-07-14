import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Predict Engagement",
    layout="wide"
)

st.title("🤖 Predict High Engagement")

st.write(
"""
Enter learner details below to predict whether the learner
belongs to the High Engagement category.
"""
)

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("models/decision_tree.pkl")

# ==========================
# USER INPUT
# ==========================

col1,col2 = st.columns(2)

with col1:

    region = st.selectbox(
        "Region",
        ["North","South","East","West"]
    )

    course = st.selectbox(
        "Course",
        [
            "Data Science",
            "AI",
            "Business Analytics",
            "Cyber Security"
        ]
    )

    pitch = st.selectbox(
        "Pitch Category",
        [
            "Consultative",
            "Promotional",
            "Informative"
        ]
    )

    script = st.selectbox(
        "Script Tone",
        [
            "Formal",
            "Friendly",
            "Persuasive"
        ]
    )

    followup = st.selectbox(
        "Follow-up Gap",
        [
            "Same Day",
            "1-2 Days",
            "3-5 Days",
            "More than 5 Days"
        ]
    )

    outreach = st.selectbox(
        "Outreach Type",
        [
            "WhatsApp",
            "Call",
            "Email"
        ]
    )

with col2:

    time_slot = st.selectbox(
        "Time Slot",
        [
            "Morning",
            "Afternoon",
            "Evening"
        ]
    )

    pitch_minutes = st.number_input(
        "Pitch Duration (minutes)",
        1.0,
        60.0,
        10.0
    )

    attempts = st.number_input(
        "Attempts",
        1,
        10,
        2
    )

    lag = st.number_input(
        "Lag",
        0,
        30,
        5
    )

    elt = st.number_input(
        "ELT",
        0,
        100,
        50
    )

    lead_score = st.slider(
        "Lead Score",
        0.0,
        100.0,
        50.0
    )

    conversion = st.slider(
        "Conversion Probability",
        0.0,
        100.0,
        50.0
    )

# ==========================
# ENCODING
# ==========================

# IMPORTANT:
# Replace these mappings with the
# exact mappings from your LabelEncoder.

region_map = {
    "East":0,
    "North":1,
    "South":2,
    "West":3
}

course_map = {
    "AI":0,
    "Business Analytics":1,
    "Cyber Security":2,
    "Data Science":3
}

time_map = {
    "Morning":0,
    "Afternoon":1,
    "Evening":2
}

pitch_map = {
    "Consultative":0,
    "Informative":1,
    "Promotional":2
}

follow_map = {
    "Same Day":0,
    "1-2 Days":1,
    "3-5 Days":2,
    "More than 5 Days":3
}

script_map = {
    "Formal":0,
    "Friendly":1,
    "Persuasive":2
}

outreach_map = {
    "Call":0,
    "Email":1,
    "WhatsApp":2
}

# ==========================
# PREDICT
# ==========================

if st.button("Predict Engagement"):

    X = pd.DataFrame({

        "Region":[region_map[region]],
        "Course":[course_map[course]],
        "Time_Slot":[time_map[time_slot]],
        "Pitch_Category":[pitch_map[pitch]],
        "Pitch_Minutes":[pitch_minutes],
        "Followup_Gap":[follow_map[followup]],
        "Script_Tone":[script_map[script]],
        "Attempts":[attempts],
        "Lag":[lag],
        "ELT":[elt],
        "Outreach_Type":[outreach_map[outreach]],
        "Lead_Score":[lead_score],
        "Conversion_Probability":[conversion]

    })

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0]

    st.divider()

    if prediction == 1:

        st.success("✅ High Engagement Predicted")

        st.metric(
            "Confidence",
            f"{probability[1]*100:.2f}%"
        )

        st.info("""
### Business Recommendation

✔ Priority Follow-up

✔ Personalized Counselling

✔ Immediate Sales Outreach

✔ High Conversion Potential
""")

    else:

        st.error("⚠ Low Engagement Predicted")

        st.metric(
            "Confidence",
            f"{probability[0]*100:.2f}%"
        )

        st.warning("""
### Business Recommendation

• Increase Follow-up Frequency

• Send Reminder Campaigns

• Improve Engagement Strategy

• Reassess Lead Quality
""")
