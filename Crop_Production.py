# CROP PRODUCTION APP ------------------ STREAMLIT

"""
Created on Sat Mar 13 19:34:17 2021

@author: rhira
"""

import streamlit as st 
import pandas as pd
import pickle
import numpy


temp_def = 1.879744
humid_def = 23.002744
ph_def= 6.502985
rain_def = 34.935536	
acidic = 0

st.header('Enter the following parameters:- ')
temp = st.text_area('temp',temp_def,height=50)
humid = st.text_area('humid input',humid_def,height=50)
ph = st.text_area('ph',ph_def,height=50)
rain = st.text_area('rain',rain_def,height=50)

if ph_def < 7.0 :
    acidic = 1
lst = [temp,humid,ph,rain]   

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
arr = numpy.array(lst).reshape(-1,1)
x = scaler.fit_transform(arr)
#print(arr)
load_clf = pickle.load(open('knn.pkl', 'rb'))
x = x.reshape(1,-1)
#print(x)
prediction = load_clf.predict(x)
#print(prediction)
st.write(prediction)



# Deploying on heroku

#d = {'Temprature':temp_def,'Humidity':humid_def,'PH':ph_def,'Rainfall':rain_def,'Acidic':acidic}
#df = pd.DataFrame(d)

#print(df.head())




