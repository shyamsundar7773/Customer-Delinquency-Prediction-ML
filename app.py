import streamlit as st


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI-Powered Customer Delinquency Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------
# Sidebar Branding
# ---------------------------------

with st.sidebar:

    st.title("🏦 Delinquency AI")

    st.markdown(
        """
        **Machine Learning Credit Risk System**

        Predict customer payment default risk
        using Artificial Intelligence.
        """
    )

    st.divider()

    st.info(
        """
        Navigate through the pages
        to explore data analysis,
        model performance and
        customer risk prediction.
        """
    )


# ---------------------------------
# Main Header
# ---------------------------------

st.title(
    "🏦 AI-Powered Customer Delinquency Prediction"
)


st.markdown(
    """
    ## Welcome 👋

    This application demonstrates an end-to-end Machine Learning
    solution for predicting customer delinquency risk using the
    **Taiwan Credit Card Default Dataset**.

    The system analyzes customer financial behaviour and predicts
    the probability of future payment default.
    """
)


st.divider()



# ---------------------------------
# Project Highlights
# ---------------------------------

st.subheader("📌 Project Highlights")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Dataset Size",
        "30,000"
    )


with col2:

    st.metric(
        "ML Model",
        "Random Forest"
    )


with col3:

    st.metric(
        "Accuracy",
        "78.18%"
    )


with col4:

    st.metric(
        "ROC-AUC",
        "77.64%"
    )


st.divider()



# ---------------------------------
# ML Workflow
# ---------------------------------

st.subheader("🔄 Machine Learning Workflow")


st.write(
    """
    ```
    Data Collection
          ↓
    Exploratory Data Analysis
          ↓
    Data Preprocessing
          ↓
    Feature Engineering
          ↓
    Model Training
          ↓
    Model Evaluation
          ↓
    Customer Risk Prediction
          ↓
    Business Insights
    ```
    """
)



st.divider()



# ---------------------------------
# Application Modules
# ---------------------------------

st.subheader("🚀 Application Modules")


modules = {
    "Module": [
        "Dataset Analysis",
        "Data Preprocessing",
        "Model Evaluation",
        "Customer Prediction",
        "Business Insights",
        "About Project"
    ],

    "Purpose": [
        "Understand customer data patterns",
        "Prepare data for ML modelling",
        "Compare machine learning models",
        "Predict individual customer risk",
        "Generate business recommendations",
        "Project documentation"
    ]
}


st.table(modules)



st.divider()



# ---------------------------------
# Navigation Note
# ---------------------------------

st.success(
    "👈 Use the sidebar to explore different sections of the AI system."
)

