

import pandas as pd
import numpy as np
import pickle

import streamlit as st
pickle_in=open('lm.pkl','rb')
lm=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(Income,Age,Rooms,Bedrooms,Population):
    

    prediction=lm.predict([[Income,Age,Rooms,Bedrooms,Population]])
    print(prediction)
    return (prediction)



def main():
    st.title('Varsha home')
    html_temp=""
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Income=float(st.text_input("Income",0))
    Age=float(st.text_input("Age",0))
    Rooms=float(st.text_input("Rooms",0))
    Bedrooms=float(st.text_input("Bedrooms",0))
    Population=float(st.text_input("Population",0))
    result=0
    if st.button("Predict"):
        
        result=predict_note_authentication(Income,Age,Rooms,Bedrooms,Population)
    st.success((format(result)))    
    if(st.button("about")):
        st.text("Lets Learn")
        st.text("built")

    



if __name__=='__main__':
     main()