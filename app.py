import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

st.set_page_config(page_title="Bank Churn Prediction", page_icon="🏦", layout="centered")
st.title("Fintech Customer Bank Exiting Prediction")

# --- Load Model and Encoders ---
@st.cache_resource
def load_resources():
    model = tf.keras.models.load_model('model.h5')
    with open('label_encoder_gender.pkl', 'rb') as file:
        label_encoder_gender = pickle.load(file)
    with open('onehot_encoder_geo.pkl', 'rb') as file:
        onehot_encoder_geo = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return model, label_encoder_gender, onehot_encoder_geo, scaler

model, label_encoder_gender, onehot_encoder_geo, scaler = load_resources()

# --- User Inputs ---
geography = st.selectbox("Geography", onehot_encoder_geo.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", 18, 92)
balance = st.number_input('Balance', min_value=0.0, step=100.0)
credit_score = st.number_input('CreditScore', min_value=300, max_value=900, step=1)
estimated_salary = st.number_input('EstimatedSalary', min_value=0.0, step=100.0)
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('NumOfProducts', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# --- Prediction ---
if st.button("Predict Churn"):
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [label_encoder_gender.transform([gender])[0]],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary]
    })

    geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
    geo_encoded_df = pd.DataFrame(
        geo_encoded,
        columns=onehot_encoder_geo.get_feature_names_out(['Geography'])
    )

    # Combine features
    input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

    # Scale input
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)
    prediction_proba = prediction[0][0]

    st.write(f"### Churn Probability: **{prediction_proba:.2f}**")

    if prediction_proba > 0.5:
        st.error("🔴 The Customer is likely to leave the bank")
    else:
        st.success("🟢 The Customer will not leave the bank")
 