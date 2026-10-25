import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('model.sav')

# Set page configuration and title
st.set_page_config(page_title="Sales Predictor", layout="centered")
st.title("📈 Sales Prediction App")
st.write("Predict sales based on advertising budgets for TV, Radio, and Newspaper.")

# Add input fields
st.sidebar.header("Advertising Budgets ($1000s)")
tv = st.sidebar.number_input("TV Budget", min_value=0.0, max_value=1000.0, value=20.0, step=1.0)
radio = st.sidebar.number_input("Radio Budget", min_value=0.0, max_value=1000.0, value=12.0, step=1.0)
newspaper = st.sidebar.number_input("Newspaper Budget", min_value=0.0, max_value=1000.0, value=5.0, step=1.0)

# Create a DataFrame for the prediction input with correct feature names
input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])

# Predict and display
if st.button("Predict Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sales: **{prediction:.2f}** units")