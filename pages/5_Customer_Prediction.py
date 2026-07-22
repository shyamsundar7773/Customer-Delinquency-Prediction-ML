import streamlit as st
import pandas as pd
import pickle


# ---------------------------------
# Page Configuration
# ---------------------------------

st.title("👤 Customer Delinquency Prediction")
st.markdown("### AI-Based Credit Risk Assessment")
st.divider()


# ---------------------------------
# Load Random Forest Pipeline
# ---------------------------------

with open("models/random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)



# ---------------------------------
# Customer Input
# ---------------------------------

st.subheader("Enter Customer Details")


col1, col2 = st.columns(2)


with col1:

    limit_bal = st.number_input(
        "Credit Limit (LIMIT_BAL)",
        min_value=1000,
        value=50000
    )


    sex = st.selectbox(
        "Gender",
        [1, 2]
    )


    education = st.selectbox(
        "Education",
        [1, 2, 3, 4]
    )


    marriage = st.selectbox(
        "Marriage Status",
        [1, 2, 3]
    )


    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )


with col2:

    pay_0 = st.number_input(
        "PAY_0 (Latest Payment Status)",
        min_value=-2,
        max_value=8,
        value=0
    )


    pay_2 = st.number_input(
        "PAY_2",
        min_value=-2,
        max_value=8,
        value=0
    )


    pay_3 = st.number_input(
        "PAY_3",
        min_value=-2,
        max_value=8,
        value=0
    )


    pay_4 = st.number_input(
        "PAY_4",
        min_value=-2,
        max_value=8,
        value=0
    )


    pay_5 = st.number_input(
        "PAY_5",
        min_value=-2,
        max_value=8,
        value=0
    )


    pay_6 = st.number_input(
        "PAY_6",
        min_value=-2,
        max_value=8,
        value=0
    )


st.divider()


# ---------------------------------
# Bill Amount Inputs
# ---------------------------------

st.subheader("Bill Amount Details")


bill_col1, bill_col2 = st.columns(2)


with bill_col1:

    bill_amt1 = st.number_input("BILL_AMT1", value=5000)
    bill_amt2 = st.number_input("BILL_AMT2", value=5000)
    bill_amt3 = st.number_input("BILL_AMT3", value=5000)

with bill_col2:

    bill_amt4 = st.number_input("BILL_AMT4", value=5000)
    bill_amt5 = st.number_input("BILL_AMT5", value=5000)
    bill_amt6 = st.number_input("BILL_AMT6", value=5000)



st.subheader("Payment Amount Details")


pay_amt1 = st.number_input("PAY_AMT1", value=2000)
pay_amt2 = st.number_input("PAY_AMT2", value=2000)
pay_amt3 = st.number_input("PAY_AMT3", value=2000)
pay_amt4 = st.number_input("PAY_AMT4", value=2000)
pay_amt5 = st.number_input("PAY_AMT5", value=2000)
pay_amt6 = st.number_input("PAY_AMT6", value=2000)



st.divider()



# ---------------------------------
# Prediction
# ---------------------------------

if st.button("🔍 Predict Customer Risk"):


    # Feature Engineering
    repayment_status = [
        pay_0,
        pay_2,
        pay_3,
        pay_4,
        pay_5,
        pay_6
    ]


    avg_repayment_status = sum(repayment_status) / 6

    maximum_repayment_delay = max(repayment_status)

    delayed_month_count = sum(
        1 for x in repayment_status if x > 0
    )


    bills = [
        bill_amt1,
        bill_amt2,
        bill_amt3,
        bill_amt4,
        bill_amt5,
        bill_amt6
    ]


    payments = [
        pay_amt1,
        pay_amt2,
        pay_amt3,
        pay_amt4,
        pay_amt5,
        pay_amt6
    ]


    average_bill_amount = sum(bills) / 6

    total_payment_amount = sum(payments)


    bill_to_limit_ratio = (
        average_bill_amount / limit_bal
        if limit_bal > 0 else 0
    )


    payment_to_bill_ratio = (
        total_payment_amount / sum(bills)
        if sum(bills) > 0 else 0
    )


    # Age Group

    if age <= 25:
        age_group = "18-25"

    elif age <= 35:
        age_group = "26-35"

    elif age <= 45:
        age_group = "36-45"

    elif age <= 60:
        age_group = "46-60"

    else:
        age_group = "60+"



    # Create DataFrame with exact features

    customer = pd.DataFrame(
        {
            "LIMIT_BAL": [limit_bal],
            "SEX": [sex],
            "EDUCATION": [education],
            "MARRIAGE": [marriage],
            "AGE": [age],

            "PAY_0": [pay_0],
            "PAY_2": [pay_2],
            "PAY_3": [pay_3],
            "PAY_4": [pay_4],
            "PAY_5": [pay_5],
            "PAY_6": [pay_6],

            "BILL_AMT1": [bill_amt1],
            "BILL_AMT2": [bill_amt2],
            "BILL_AMT3": [bill_amt3],
            "BILL_AMT4": [bill_amt4],
            "BILL_AMT5": [bill_amt5],
            "BILL_AMT6": [bill_amt6],

            "PAY_AMT1": [pay_amt1],
            "PAY_AMT2": [pay_amt2],
            "PAY_AMT3": [pay_amt3],
            "PAY_AMT4": [pay_amt4],
            "PAY_AMT5": [pay_amt5],
            "PAY_AMT6": [pay_amt6],

            "Average_Repayment_Status": [
                avg_repayment_status
            ],

            "Maximum_Repayment_Delay": [
                maximum_repayment_delay
            ],

            "Delayed_Month_Count": [
                delayed_month_count
            ],

            "Average_Bill_Amount": [
                average_bill_amount
            ],

            "Total_Payment_Amount": [
                total_payment_amount
            ],

            "Bill_to_Limit_Ratio": [
                bill_to_limit_ratio
            ],

            "Payment_to_Bill_Ratio": [
                payment_to_bill_ratio
            ],

            "Age_Group": [
                age_group
            ]
        }
    )


    # Prediction

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0][1]


    st.divider()

    st.subheader("Prediction Result")


    st.metric(
        "Default Probability",
        f"{probability:.2%}"
    )


    if prediction == 1:

        st.error(
            "Customer Risk Level: High Risk 🔴"
        )

        st.write(
            """
            Recommended Actions:

            - Contact customer for payment follow-up
            - Provide repayment assistance
            - Closely monitor future transactions
            """
        )


    else:

        st.success(
            "Customer Risk Level: Low Risk 🟢"
        )

        st.write(
            """
            Recommended Actions:

            - Continue regular monitoring
            - Maintain customer relationship
            - Offer suitable financial services
            """
        )


    st.subheader("Customer Feature Summary")

    st.dataframe(
        customer,
        width="stretch"
    )