import streamlit as st
import pandas as pd
import joblib

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Predict High Engagement",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 High Engagement Prediction")

st.write(
"""
Predict whether a learner is likely to belong to the **High Engagement**
category using the trained Decision Tree model.
"""
)

# ----------------------------------
# LOAD MODEL & ENCODERS
# ----------------------------------

model = joblib.load("decision_tree.pkl")

encoders = joblib.load("encoders.pkl")

# ----------------------------------
# USER INPUT
# ----------------------------------

c1,c2 = st.columns(2)

with c1:

    region = st.selectbox(
        "Region",
        encoders["Region"].classes_
    )

    course = st.selectbox(
        "Course",
        encoders["Course"].classes_
    )

    time_slot = st.selectbox(
        "Time Slot",
        encoders["Time_Slot"].classes_
    )

    pitch = st.selectbox(
        "Pitch Category",
        encoders["Pitch_Category"].classes_
    )

    followup = st.selectbox(
        "Follow-up Gap",
        encoders["Followup_Gap"].classes_
    )

    script = st.selectbox(
        "Script Tone",
        encoders["Script_Tone"].classes_
    )

with c2:

    outreach = st.selectbox(
        "Outreach Type",
        encoders["Outreach_Type"].classes_
    )

    pitch_minutes = st.number_input(
        "Pitch Duration",
        value=10.0
    )

    attempts = st.number_input(
        "Attempts",
        value=2
    )

    lag = st.number_input(
        "Lag",
        value=5
    )

    elt = st.number_input(
        "ELT",
        value=60
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

# ----------------------------------
# PREDICT
# ----------------------------------

if st.button("Predict"):

    row = pd.DataFrame({

        "Region":[
            encoders["Region"].transform([region])[0]
        ],

        "Course":[
            encoders["Course"].transform([course])[0]
        ],

        "Time_Slot":[
            encoders["Time_Slot"].transform([time_slot])[0]
        ],

        "Pitch_Category":[
            encoders["Pitch_Category"].transform([pitch])[0]
        ],

        "Pitch_Minutes":[pitch_minutes],

        "Followup_Gap":[
            encoders["Followup_Gap"].transform([followup])[0]
        ],

        "Script_Tone":[
            encoders["Script_Tone"].transform([script])[0]
        ],

        "Attempts":[attempts],

        "Lag":[lag],

        "ELT":[elt],

        "Outreach_Type":[
            encoders["Outreach_Type"].transform([outreach])[0]
        ],

        "Lead_Score":[lead_score],

        "Conversion_Probability":[conversion]

    })

    prediction = model.predict(row)[0]

    probability = model.predict_proba(row)

    confidence = round(
        probability.max()*100,
        2
    )

    st.markdown("---")

    if prediction == 1:

        st.success("✅ High Engagement Predicted")

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

        st.info("""
### Recommendation

✔ Immediate Follow-up

✔ Priority Counselling

✔ High Conversion Potential

✔ Allocate Sales Executive
""")

    else:

        st.error("⚠ Low Engagement Predicted")

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

        st.warning("""
### Recommendation

• Increase Follow-up

• Send Reminder Messages

• Improve Outreach Strategy

• Reassess Lead Quality
""")

st.markdown("---")

st.subheader("Model Information")

st.write("""
**Algorithm Used**

- Decision Tree Classifier

**Target Variable**

- High Engagement

**Input Features**

- Region
- Course
- Time Slot
- Pitch Category
- Pitch Duration
- Follow-up Gap
- Script Tone
- Attempts
- Lag
- ELT
- Outreach Type
- Lead Score
- Conversion Probability
""")
