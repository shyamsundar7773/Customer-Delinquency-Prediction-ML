import streamlit as st
import pandas as pd
import plotly.express as px

from utils.loader import load_data


# -----------------------------
# Page Configuration
# -----------------------------

st.title("📈 Business Insights")
st.markdown("### AI-Driven Credit Risk Insights & Recommendations")
st.divider()


# -----------------------------
# Load Dataset
# -----------------------------

df = load_data()


target = "default.payment.next.month"


# -----------------------------
# Portfolio Overview
# -----------------------------

st.subheader("💳 Customer Portfolio Overview")


total_customers = len(df)

default_customers = df[target].sum()

non_default_customers = total_customers - default_customers


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Customers",
        f"{total_customers:,}"
    )


with col2:

    st.metric(
        "Default Customers",
        f"{default_customers:,}"
    )


with col3:

    default_rate = (
        default_customers / total_customers
    ) * 100

    st.metric(
        "Default Rate",
        f"{default_rate:.2f}%"
    )


st.divider()



# -----------------------------
# Default Distribution
# -----------------------------

st.subheader("Customer Default Distribution")


distribution = pd.DataFrame(
    {
        "Status": [
            "Non Default",
            "Default"
        ],

        "Customers": [
            non_default_customers,
            default_customers
        ]
    }
)


fig = px.pie(
    distribution,
    names="Status",
    values="Customers",
    title="Default vs Non Default Customers"
)


st.plotly_chart(
    fig,
    width="stretch"
)



st.divider()



# -----------------------------
# Risk Factors
# -----------------------------

st.subheader("⚠️ Key Risk Factors")


risk_data = pd.DataFrame(
    {
        "Risk Factor": [
            "Delayed Payments",
            "High Credit Utilization",
            "Low Payment Amount",
            "Previous Default History"
        ],

        "Impact": [
            "High",
            "High",
            "Medium",
            "High"
        ]
    }
)


st.dataframe(
    risk_data,
    width="stretch"
)



st.divider()



# -----------------------------
# Payment Behaviour Analysis
# -----------------------------

st.subheader("Payment Behaviour Analysis")


payment_chart = px.histogram(
    df,
    x="PAY_0",
    title="Latest Payment Status Distribution"
)


st.plotly_chart(
    payment_chart,
    width="stretch"
)



st.divider()



# -----------------------------
# Business Recommendations
# -----------------------------

st.subheader("💡 Business Recommendations")


st.success(
    """
    Recommended Strategies:

    1. Early Risk Detection
       - Identify customers showing delayed payment behaviour.

    2. Proactive Customer Engagement
       - Send reminders before accounts become delinquent.

    3. Personalized Repayment Plans
       - Provide flexible repayment options for high-risk customers.

    4. Continuous Monitoring
       - Use AI predictions for regular credit risk assessment.

    5. Improve Collection Efficiency
       - Prioritize high-risk customers instead of contacting all customers equally.
    """
)