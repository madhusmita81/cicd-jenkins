from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from package_ml.predict import generate_predictions

app= FastAPI(
    title= "Loan Prediction App using Jenkins",
    description= "A simple CI Cd demo",
    version= "1.o"
)

origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoanPrediction(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str   

@app.get("/")
def index():
    return {"message" : "Loan Prediction App using Jenkins"}

@app.post("/prediction_api")
def predict(loan_details: LoanPrediction):
    data= loan_details.model_dump()
    pred= generate_predictions([data])["prediction"][0]
    if pred == "Y":
        result= "approved"
    else:
        result= "rejected"
    
    return {"status": result}

@app.post("/prediction_ui")
def predict_gui(Gender: str,
    Married: str,
    Dependents: str,
    Education: str,
    Self_Employed: str,
    ApplicantIncome: float,
    CoapplicantIncome: float,
    LoanAmount: float,
    Loan_Amount_Term: float,
    Credit_History: float,
    Property_Area: str):
    input_data = [Gender, Married,Dependents, Education, Self_Employed,ApplicantIncome,
     CoapplicantIncome,LoanAmount, Loan_Amount_Term,Credit_History, Property_Area  ]
    
    cols= ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    
    data_dict= dict(zip(cols, input_data))
    pred= generate_predictions([data_dict])["prediction"][0]
    if pred == "Y":
        result= "approved"
    else:
        result= "rejected"
    
    return {"status": result}

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port= 8005)
    # uvicorn.run(app)
