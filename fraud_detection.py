import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("fraud_detection_pipeline.pkl")    

st.title("Credit Card Fraud Detection App")
st.markdown("Enter the transaction details below to predict if it's fraudulent or not.")
st.divider()



# Input fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)

if st.button("Predict"):
    input_data = {
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }
    
    # CRITICAL: Convert dictionary to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(input_df)
    
    if prediction[0] == 1:
        st.error("🚨 Warning: Fraud Detected!")
    else:

        st.success("✅ Transaction is Legitimate.")
