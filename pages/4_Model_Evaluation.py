import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page Configuration
# -----------------------------

st.title("🤖 Model Evaluation")
st.markdown("### AI Delinquency Prediction Model Performance")
st.divider()


# -----------------------------
# Model Performance Data
# -----------------------------

model_results = pd.DataFrame(
    {
        "Model": [
            "XGBoost",
            "Random Forest",
            "Decision Tree",
            "Logistic Regression"
        ],

        "Accuracy": [
            0.7592,
            0.7818,
            0.7332,
            0.7440
        ],

        "Precision": [
            0.4667,
            0.5059,
            0.4305,
            0.4420
        ],

        "Recall": [
            0.6232,
            0.5787,
            0.6390,
            0.6006
        ],

        "F1 Score": [
            0.5337,
            0.5399,
            0.5144,
            0.5093
        ],

        "ROC-AUC": [
            0.7766,
            0.7764,
            0.7550,
            0.7475
        ],

        "PR-AUC": [
            0.5544,
            0.5550,
            0.5164,
            0.4982
        ]
    }
)


# -----------------------------
# Model Comparison
# -----------------------------

st.subheader("📊 Model Comparison Table")


st.dataframe(
    model_results,
    width="stretch"
)


st.divider()


# -----------------------------
# Selected Model
# -----------------------------

selected_model = model_results[
    model_results["Model"] == "Random Forest"
].iloc[0]


st.subheader("🏆 Selected Model")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Final Model",
        selected_model["Model"]
    )


with col2:
    st.metric(
        "Accuracy",
        f"{selected_model['Accuracy']:.2%}"
    )


with col3:
    st.metric(
        "F1 Score",
        f"{selected_model['F1 Score']:.4f}"
    )


st.divider()


# -----------------------------
# Performance Metrics Chart
# -----------------------------

st.subheader("Model Performance Comparison")


performance_chart = px.bar(
    model_results,
    x="Model",
    y=[
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ],
    barmode="group",
    title="Comparison of Evaluation Metrics"
)


st.plotly_chart(
    performance_chart,
    width="stretch"
)


st.divider()


# -----------------------------
# ROC-AUC and PR-AUC Comparison
# -----------------------------

st.subheader("ROC-AUC and PR-AUC Comparison")


auc_chart = px.bar(
    model_results,
    x="Model",
    y=[
        "ROC-AUC",
        "PR-AUC"
    ],
    barmode="group",
    title="Model Ranking Based on AUC Metrics"
)


st.plotly_chart(
    auc_chart,
    width="stretch"
)


st.divider()


# -----------------------------
# Classification Report
# -----------------------------

st.subheader("📋 Random Forest Classification Report")


classification_report = pd.DataFrame(
    {
        "Class": [
            "0 - Non Default",
            "1 - Default"
        ],

        "Precision": [
            0.875,
            0.506
        ],

        "Recall": [
            0.840,
            0.579
        ],

        "F1 Score": [
            0.857,
            0.540
        ],

        "Support": [
            4673,
            1327
        ]
    }
)


st.dataframe(
    classification_report,
    width="stretch"
)


st.divider()


# -----------------------------
# Business Interpretation
# -----------------------------

st.subheader("📌 Business Interpretation")


st.write(
    """
    - Accuracy represents the overall correctness of predictions.

    - Precision shows how accurately the model identifies customers
      who are actually likely to default.

    - Recall is important in credit risk because it helps identify
      more potential delinquent customers.

    - F1 Score provides a balance between precision and recall.

    - Random Forest is selected as the final model because it provides
      the best overall balance of accuracy, precision, F1-score and PR-AUC.

    - The model can support proactive customer risk management
      and early intervention strategies.
    """
)