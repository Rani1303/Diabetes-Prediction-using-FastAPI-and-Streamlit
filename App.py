import streamlit as st
import requests
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
def main():
    st.markdown("""<h1 style='text-align: center; color: #008080;'>Diabetes Prediction</h1>""", unsafe_allow_html=True)

    st.header("Enter Patient Information:")
    pregnancies = st.number_input("Pregnancies", min_value=0, value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0, value=0, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=0, step=1)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=0, step=1)
    insulin = st.number_input("Insulin", min_value=0, value=0, step=1)
    bmi = st.number_input("BMI", min_value=0.0, value=0.0, step=1.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.0, step=1.0)
    age = st.number_input("Age", min_value=0, value=0, step=1)

    if st.button("Predict", key="prediction_button"):
        if all([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi]) and all([dpf, age]):
            with st.spinner("Predicting..."):
                input_data = ModelInput(
                    Pregnancies=pregnancies,
                    Glucose=glucose,
                    BloodPressure=blood_pressure,
                    SkinThickness=skin_thickness,
                    Insulin=insulin,
                    BMI=bmi,
                    DiabetesPedigreeFunction=dpf,
                    Age=age,
                )
                input_data_json = jsonable_encoder(input_data)

                response = requests.get("http://127.0.0.1:8000/diabetes_prediction", json=input_data_json)

            st.success(f"Prediction Result: {response.text}")
        else:
            st.error("Please input details before predicting.")


if __name__ == "__main__":
    main()
