#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')


# Render About page
@app.route('/about')
def about():
    return render_template('about.html')


# Prediction Page
@app.route('/predict', methods = ["GET","POST"])
def predict():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        print("Len of features: {0}", len(float_features))
        print(float_features)
        Term = float_features[0]
        GrAppv = float_features[1]
        SBA_Appv = float_features[2]
        NoEmp = float_features[3]
        RetainedJob = float_features[4]
        CreateJob = float_features[5]
        RevLineCr = float_features[6]
        
        





        features = np.array(float_features).reshape(-1, 7)
        prediction = model.predict(features)

        # GrAppv=input['GrAppv']
        # SBA_Appv = input['SBA_Appv']
        # RevLineCr = input['RevLineCr_Y']
        # NoEmp = input['NoEmp']
        # CreateJob = input['CreateJob']
        # RetainedJob = input['RetainedJob']
        # features = np.array(float_features).reshape((1,-1))
        # prediction = model.predict(features)
        # return render_template('result.html', data=input, prediction=prediction)
        return render_template('result.html',data=input, prediction=prediction,Term=Term,GrAppv = GrAppv, SBA_Appv = SBA_Appv,NoEmp = NoEmp, RetainedJob = RetainedJob, CreateJob = CreateJob, RevLineCr = RevLineCr )
        # return redirect(url_for('result'))

        # show the form, it wasn't submitted
    return render_template('predict.html')

    # return render_template('result.html',data=input, prediction=prediction, Term=input['Term'],
    #     GrAppv=input['GrAppv'],
    #     SBA_Appv=input['SBA_Appv'], RevLineCr=input['RevLineCr_Y'],
    #     NoEmp=input['NoEmp'],CreateJob=input['CreateJob'],RetainedJob=input['RetainedJob'])



if __name__ == "__main__":
    app.run(debug=True, port=5000)


# %%
