import streamlit as st
import pandas as pd


# Load Data with Caching
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Kevin-0510/my-streamlit-app/main/cleaned_ckd_data_fixed.csv"
    df = pd.read_csv(url)
    st.write("Dataset Loaded Successfully!")  # Debugging statement
    return df


ckd_df = load_data()


# Function to get diet recommendation
def get_diet_recommendation(ckd_stage):
    if ckd_stage == "Stage 1":
        return "Maintain a balanced diet."
    elif ckd_stage == "Stage 2":
        return "Low protein intake recommended."
    elif ckd_stage == "Stage 3":
        return "Limit phosphorus and potassium."
    elif ckd_stage == "Stage 4":
        return "Low sodium and potassium diet required."
    elif ckd_stage == "Stage 5":
        return "Strict renal diet required."
    else:
        return "Unknown CKD Stage."


# Function to predict CKD stage & diet recommendation
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

# Get Patient ID Input
patient_id = st.number_input("Enter Patient ID:", min_value=1, step=1)

if st.button("Predict"):
    result = predict_ckd_and_diet(patient_id)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"Patient ID: {result['Patient ID']}")
        st.info(f"CKD Stage: {result['CKD Stage']}")
        st.warning(f"Diet Recommendation: {result['Diet Recommendation']}")
