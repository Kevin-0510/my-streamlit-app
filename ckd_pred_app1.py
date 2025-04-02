
import streamlit as st
import pandas as pd

# Load CKD dataset (Make sure to upload 'ckd_data.csv' in Colab)
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_ckd_data_fixed.csv")

ckd_df = load_data()

# Function to predict CKD stage & suggest diet
def get_diet_recommendation(ckd_stage):
    if "Stage 1" in ckd_stage:
        return "Maintain a balanced diet."
    elif "Stage 2" in ckd_stage:
        return "Low protein intake recommended."
    elif "Stage 3" in ckd_stage:
        return "Limit phosphorus and potassium."
    elif "Stage 4" in ckd_stage:
        return "Low sodium and potassium diet required."
    else:
        return "Strict renal diet required."

def predict_ckd_and_diet(patient_id):
    patient_data = ckd_df[ckd_df['id'] == patient_id]
    if patient_data.empty:
        return {"error": "Patient ID not found."}

    ckd_stage = patient_data['CKD_Stage'].values[0]
    diet_recommendation = get_diet_recommendation(ckd_stage)

    return {
        "Patient ID": patient_id,
        "CKD Stage": ckd_stage,
        "Diet Recommendation": diet_recommendation
    }

# Streamlit Web App UI
st.title("CKD Prediction & Diet Recommendation")

patient_id = st.number_input("Enter Patient ID:", min_value=1, step=1)
if st.button("Predict"):
    result = predict_ckd_and_diet(patient_id)
    
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"Patient ID: {result['Patient ID']}")
        st.info(f"CKD Stage: {result['CKD Stage']}")
        st.warning(f"Diet Recommendation: {result['Diet Recommendation']}")
