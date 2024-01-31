from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


app = FastAPI()

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int       
        
# loading the saved model
with open('diabetes_model.pkl','rb') as f:
    model=pickle.load(f)

@app.get('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    df = pd.DataFrame([input_parameters.dict().values()], columns=input_parameters.dict().keys())
    yhat=model.predict(df)

    if yhat[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    



