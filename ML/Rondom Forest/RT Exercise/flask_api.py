# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: krish.naik
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

with open("C:/Users/navne/OneDrive/Desktop/Test Jupyter/ML/Rondom Forest/RT Exercise/classifier.pkl", "rb") as read_file:
          model = pickle.load(read_file)
    

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    
    sepal_length=request.args.get("sepal length (cm)")
    sepal_width=request.args.get("sepal width (cm)")
    petal_length=request.args.get("petal length (cm)")
    petal_width=request.args.get("petal width (cm)")
    
    prediction=model.predict([["sepal length (cm)", "sepal width (cm)", "petal length (cm)" , "petal width (cm)"]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    