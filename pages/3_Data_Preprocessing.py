import streamlit as st
import pandas as pd

from utils.loader import load_data


# -----------------------------
# Page Configuration
# -----------------------------

st.title("🧹 Data Preprocessing")
st.markdown("### Taiwan Credit Card Default Dataset")
st.divider()


# -----------------------------
# Load Dataset
# -----------------------------

df = load_data()


# Keep original copy
original_df = df.copy()


# -----------------------------
# Dataset Before Cleaning
# -----------------------------

st.subheader("Dataset Before Cleaning")


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
# Missing Value Analysis
# -----------------------------

st.subheader("Missing Value Analysis")


missing_df = pd.DataFrame(
    {
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    }
)


missing_df = missing_df[
    missing_df["Missing Values"] > 0
]


if len(missing_df) == 0:

    st.success(
        "No missing values found in dataset ✅"
    )

else:

    st.dataframe(
        missing_df,
        width="stretch"
    )


st.divider()


# -----------------------------
# Duplicate Removal
# -----------------------------

st.subheader("Duplicate Row Analysis")


duplicate_count = df.duplicated().sum()


if duplicate_count > 0:

    st.warning(
        f"{duplicate_count} duplicate rows detected"
    )

    df = df.drop_duplicates()

    st.success(
        "Duplicate rows removed successfully ✅"
    )

else:

    st.success(
        "No duplicate rows found ✅"
    )


st.divider()


# -----------------------------
# Feature Target Separation
# -----------------------------

st.subheader("Feature and Target Separation")


target_column = "default.payment.next.month"


if target_column in df.columns:

    X = df.drop(
        target_column,
        axis=1
    )

    y = df[target_column]


    col1, col2 = st.columns(2)


    with col1:

        st.info(
            f"Features (X): {X.shape[1]} columns"
        )


    with col2:

        st.info(
            f"Target (y): {target_column}"
        )


    st.dataframe(
        X.head(),
        width="stretch"
    )


else:

    st.error(
        "Target column not found"
    )


st.divider()


# -----------------------------
# Data Transformation Preview
# -----------------------------

st.subheader("Data Transformation")


st.write(
    """
    Machine Learning models require numerical and
    scaled data for better performance.
    
    Applied preprocessing steps:
    
    ✅ Duplicate removal
    
    ✅ Feature separation
    
    ✅ Standardization preparation
    
    ✅ Train-test split preparation
    """
)


st.divider()


# -----------------------------
# Final Dataset Status
# -----------------------------

st.subheader("Final Dataset Status")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Final Rows",
        f"{df.shape[0]:,}"
    )


with col2:

    st.metric(
        "Final Features",
        df.shape[1]-1
    )


with col3:

    st.metric(
        "Status",
        "Ready for ML ✅"
    )