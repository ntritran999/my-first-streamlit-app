import streamlit as st
import pickle
import numpy as np

st.title("Revenue Prediction")
x_new = st.number_input("Input temperature")

if st.button("Predict"):
    model = pickle.load(open('model.pickle', "rb"))
    y_new = model.predict(np.array(x_new).reshape(-1,1))[0]
    st.write("Revenue Prediction")
    st.success(f'{y_new}')
