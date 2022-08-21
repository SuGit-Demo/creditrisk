from flask import Flask, request, jsonify, url_for, redirect, render_template
import numpy as np
import pickle
import requests
import ibm_db

app = Flask(__name__)
model = pickle.load(open('model.h5','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Gender = request.form.get('gender')
    Appincome = request.form.get('appincome')
    Coincome = request.form.get('coincome')
    LoanAmount = request.form.get('amount')
    LoanDuration = request.form.get('duration')              
   
    ##Test model prediction with static data. Reshape to change to 2D array 
    testdata = np.reshape([
    Gender,
    MStatus, #Married. Change to 0 to get No Risk. Change to 1 to get Risk
    None,
    None,
    None,
    Appincome,
    Coincome,
    LoanAmount,
    LoanDuration,
    None,
    None,
    None
    ],(1, -1))

    pred_result = model.predict(testdata)

    if(pred_result[0]==0):
        txt = 'No Risk Loan'
    else:
        txt = 'Risky Loan'
    print(txt)
    
    return render_template('index.html', prediction_text='Loan Risk Prediction is: {}'.format(txt))

if __name__ == "__main__":
    app.run()
