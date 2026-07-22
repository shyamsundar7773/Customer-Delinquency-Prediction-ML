import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------

st.title("📘 About The Project")
st.markdown("### AI-Powered Customer Delinquency Prediction System")
st.divider()


# -----------------------------
# Project Objective
# -----------------------------

st.subheader("🎯 Project Objective")

st.write(
    """
    The objective of this project is to develop an AI-powered
    customer delinquency prediction system that identifies
    customers who are likely to default on their credit payments.

    The system helps financial institutions take proactive
    actions by detecting high-risk customers early and improving
    collection strategies.
    """
)


st.divider()


# -----------------------------
# Business Problem
# -----------------------------

st.subheader("💼 Business Problem")

st.write(
    """
    Credit card companies face challenges in identifying customers
    who may fail to repay their outstanding balances.

    Traditional approaches depend on manual analysis, which can be
    time-consuming and less effective.

    This project uses machine learning techniques to predict
    delinquency risk and support data-driven decision making.
    """
)


st.divider()


# -----------------------------
# Dataset Information
# -----------------------------

st.subheader("📂 Dataset Information")


st.write(
    """
    Dataset:
    Taiwan Credit Card Default Dataset

    Source:
    UCI Machine Learning Repository

    Dataset Size:
    30,000 customer records

    Target Variable:
    default.payment.next.month

    Prediction:
    0 → Customer will not default

    1 → Customer will default
    """
)


st.divider()


# -----------------------------
# Technology Stack
# -----------------------------

st.subheader("🛠 Technology Stack")


tech = {
    "Category": [
        "Programming Language",
        "Data Processing",
        "Machine Learning",
        "Visualization",
        "Deployment"
    ],

    "Tools Used": [
        "Python",
        "Pandas, NumPy",
        "Scikit-Learn, Random Forest",
        "Plotly, Streamlit",
        "Streamlit Cloud"
    ]
}


st.table(tech)



st.divider()


# -----------------------------
# Machine Learning Workflow
# -----------------------------

st.subheader("🤖 Machine Learning Workflow")


st.write(
    """
    1. Business Understanding

    2. Data Collection

    3. Exploratory Data Analysis

    4. Data Cleaning and Preprocessing

    5. Feature Engineering

    6. Model Training

    7. Model Evaluation

    8. Customer Risk Prediction

    9. Business Recommendation
    """
)



st.divider()


# -----------------------------
# Final Model
# -----------------------------

st.subheader("🏆 Final Model")


st.success(
    """
    Selected Model: Random Forest Classifier

    Performance:

    Accuracy: 78.18%

    Precision: 50.59%

    Recall: 57.87%

    F1 Score: 53.99%

    ROC-AUC: 77.64%

    The Random Forest model was selected because it provides
    a balanced performance between identifying risky customers
    and reducing incorrect predictions.
    """
)


st.divider()


# -----------------------------
# Project Outcomes
# -----------------------------

st.subheader("📌 Project Outcomes")


st.write(
    """
    ✔ Automated customer risk prediction

    ✔ Improved identification of potential defaulters

    ✔ Supported proactive collection strategies

    ✔ Reduced dependency on manual analysis

    ✔ Enabled data-driven financial decisions
    """
)


st.divider()


# -----------------------------
# Future Enhancements
# -----------------------------

st.subheader("🚀 Future Enhancements")


st.write(
    """
    • Deploy the application on cloud infrastructure

    • Add real-time customer transaction monitoring

    • Implement explainable AI techniques such as SHAP

    • Integrate automated notification systems

    • Continuously retrain the model with new customer data
    """
)