# OutreachIQ
AI Powered Outreach Analytics Platform
Overview

OutreachIQ is an end-to-end Business Analytics application developed as part of the Summer Internship Project at TechnGlobal Private Limited. The platform integrates CRM concepts, outreach automation, statistical analysis, machine learning, and business intelligence to optimize learner engagement and lead management within the EdTech sector.

The application provides decision-makers with actionable insights by analyzing learner outreach data, identifying significant engagement factors, predicting highly engaged learners, and segmenting learners for targeted outreach strategies.

---

Key Features

- 📊 Interactive Business Intelligence Dashboard
- 📈 Exploratory Data Analysis (EDA)
- 📉 Correlation & Distribution Analysis
- 🧪 Statistical Testing
  - ANOVA
  - Chi-Square Test
  - Independent Samples T-Test
- 🤖 Predictive Analytics
  - Logistic Regression
  - Decision Tree Classifier
- 👥 Learner Segmentation using K-Means Clustering
- 📋 Automated Business Recommendations
- 📁 CSV Dataset Upload Support
- 📌 Interactive Visualizations

---

Business Objectives

The project aims to:

- Improve learner outreach efficiency.
- Identify factors influencing learner engagement.
- Predict highly engaged learners.
- Support lead prioritization using machine learning.
- Enable data-driven decision making through interactive dashboards.
- Optimize outreach operations using automation and analytics.

---

Dataset

The analysis was performed on approximately 5,000 learner records containing outreach and engagement-related attributes, including:

- Region
- Course
- Time Slot
- Pitch Category
- Pitch Duration
- Script Tone
- Follow-up Gap
- Outreach Type
- Attempts
- Lag
- ELT
- Lead Score
- Conversion Probability
- Engagement Score
- High Engagement (Target Variable)

---

Machine Learning Models

Classification

- Logistic Regression
- Decision Tree Classifier

Target Variable:

- High Engagement

Clustering

- K-Means Clustering

Segmentation Variables:

- Engagement Score
- Lag
- Attempts

---

Statistical Analysis

The application includes:

- Exploratory Data Analysis
- Distribution Analysis
- Correlation Analysis
- ANOVA
- Chi-Square Test
- Independent Samples T-Test

These analyses were performed to validate business hypotheses and identify statistically significant factors affecting learner engagement.

---

Business Outcomes

The project demonstrated measurable operational improvements:

- Analyzed 5,000+ learner records
- Reduced outreach execution time by 66.7%
- Increased outreach productivity by 60%
- Identified Follow-Up Gap as the strongest engagement factor through ANOVA
- Developed learner segmentation for targeted outreach
- Automated repetitive outreach workflows
- Enabled evidence-based lead prioritization

---

Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Plotly
- Joblib
- OpenPyXL

---

Project Structure

OutreachIQ/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── learner_data.csv
│
├── models/
│   ├── logistic_model.pkl
│   ├── decision_tree.pkl
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── pages/
│   ├── Dashboard.py
│   ├── Analytics.py
│   ├── Prediction.py
│   ├── Segmentation.py
│   ├── Automation.py
│   └── About.py
│
├── assets/
│   └── logo.png
│
└── utils/
    ├── preprocessing.py
    └── helper.py

---

Installation

Clone the repository:

git clone https://github.com/your-username/OutreachIQ.git

Navigate to the project directory:

cd OutreachIQ

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

---

Application Modules

Dashboard

Displays key business metrics, learner statistics, and interactive visualizations.

Analytics

Provides EDA, correlation heatmaps, distribution plots, and statistical analysis results.

Prediction

Predicts whether a learner belongs to the High Engagement category using trained machine learning models.

Segmentation

Groups learners into meaningful clusters using K-Means clustering to support personalized outreach strategies.

Automation

Demonstrates the outreach workflow and automation framework developed during the internship.

About

Provides project details, methodology, objectives, and business impact.

---

Future Enhancements

- Real-time CRM integration
- WhatsApp API integration
- Advanced machine learning models (Random Forest, XGBoost)
- Natural Language Processing for learner feedback
- Real-time business intelligence dashboards
- Automated recommendation engine
- Cloud database integration

---

Author

Kaustav Chakraborty
---

License

This project has been developed for academic and educational purposes as part of the MBA Summer Internship Project.
