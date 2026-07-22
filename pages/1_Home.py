import streamlit as st

# ======================================================
# Custom CSS
# ======================================================

st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:700;
    color:#0A4FAF;
}

.sub-title{
    font-size:22px;
    color:#555555;
}

.info-box{
    background-color:#F5F9FF;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #0A4FAF;
}

.footer-box{
    background-color:#F8F9FA;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# Header
# ======================================================

st.markdown(
    "<div class='main-title'>🏦 AI-Powered Customer Delinquency Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Professional Banking Analytics Dashboard</div>",
    unsafe_allow_html=True
)

st.divider()

# ======================================================
# KPI Metrics
# ======================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", "30,000")

with col2:
    st.metric("Final Model", "Random Forest")

with col3:
    st.metric("Prediction", "Binary")

with col4:
    st.metric("Dataset", "Taiwan Credit Card")

st.divider()

# ======================================================
# Overview & Business Objective
# ======================================================

left, right = st.columns([2, 1])

with left:

    st.subheader("📌 Project Overview")

    st.write("""
This project predicts customer credit card delinquency using
Machine Learning.

Multiple classification algorithms were trained and evaluated,
and **Random Forest** was selected as the final deployment model
based on overall performance metrics.

The solution helps financial institutions identify high-risk
customers and support better credit risk management.
""")

with right:

    st.subheader("🎯 Business Objective")

    st.success("""
✔ Reduce financial risk

✔ Identify default customers

✔ Improve lending decisions

✔ Support banking analytics
""")

st.divider()

# ======================================================
# Technologies
# ======================================================

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("Python")

tech2.info("Scikit-Learn")

tech3.info("Streamlit")

tech4.info("Random Forest")

st.divider()

# ======================================================
# Workflow
# ======================================================

st.subheader("🔄 Project Workflow")

workflow = [
    "Business Understanding",
    "Data Collection",
    "Exploratory Data Analysis",
    "Data Cleaning",
    "Feature Engineering",
    "Train-Test Split",
    "Model Training",
    "Model Evaluation",
    "Customer Prediction"
]

for step in workflow:
    st.write(f"✅ {step}")

st.divider()

# ======================================================
# Dashboard Features
# ======================================================

st.subheader("⭐ Dashboard Features")

col1, col2 = st.columns(2)

with col1:
    st.write("📊 Dataset Analysis")
    st.write("🧹 Data Preprocessing")
    st.write("📈 Model Evaluation")
    st.write("🤖 Machine Learning")

with col2:
    st.write("💳 Customer Prediction")
    st.write("💼 Business Insights")
    st.write("📑 Professional Dashboard")
    st.write("🚀 Deployment Ready")

st.divider()

# ======================================================
# Navigation
# ======================================================

st.info("👈 Use the sidebar to navigate through all dashboard pages.")