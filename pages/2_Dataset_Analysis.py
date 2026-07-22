import streamlit as st
import pandas as pd
import plotly.express as px

from utils.loader import load_data


# -----------------------------
# Page Configuration
# -----------------------------

st.title("📊 Dataset Analysis")
st.markdown("### Taiwan Credit Card Default Dataset")
st.divider()


# -----------------------------
# Load Dataset
# -----------------------------

df = load_data()


# -----------------------------
# Dashboard Metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )


with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )


with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )


with col4:
    st.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )


st.divider()


# -----------------------------
# Dataset Preview
# -----------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    width="stretch"
)


st.divider()


# -----------------------------
# Target Distribution
# -----------------------------

st.subheader("Target Distribution")

target_col = "default.payment.next.month"


if target_col in df.columns:

    fig = px.histogram(
        df,
        x=target_col,
        color=target_col,
        text_auto=True,
        title="Default Payment Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

else:
    st.warning(
        "Target column not found in dataset"
    )


st.divider()


# -----------------------------
# Age Distribution
# -----------------------------

st.subheader("Age Distribution")


if "AGE" in df.columns:

    fig = px.histogram(
        df,
        x="AGE",
        nbins=30,
        title="Customer Age Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

else:
    st.error(
        "AGE column not available"
    )


st.divider()


# -----------------------------
# Credit Limit Distribution
# -----------------------------

st.subheader("Credit Limit Distribution")


if "LIMIT_BAL" in df.columns:

    fig = px.histogram(
        df,
        x="LIMIT_BAL",
        nbins=40,
        title="Credit Limit Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

else:
    st.error(
        "LIMIT_BAL column not available"
    )


st.divider()


# -----------------------------
# Summary Statistics
# -----------------------------

st.subheader("Summary Statistics")


st.dataframe(
    df.describe(),
    width="stretch"
)