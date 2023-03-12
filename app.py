import streamlit as st
import pickle

st.title("Revenue Prediction")
x_new = st.number_input("Input temperature")

if st.button("Predict"):
    model = pickle.load(open('model.pickle', "rb"))
    y_new = model.predict(np.array(x_new).reshape(-1,1))
    st.success(f'Phương trình có 1 nghiệm {y_new}')

