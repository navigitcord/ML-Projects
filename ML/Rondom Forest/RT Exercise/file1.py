import numpy as np
import pickle
import pandas as pd

import streamlit as st

from PIL import Image

pickle_in = open("classifier.pkl", "rb")
model = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    print(prediction)
    return prediction


def main():
    st.title("Iris Flower Detector")
    html_temp = """
    <div style="background-color:tomato; padding:10px"> 
    <h2 style="color:white; text-align:center;">Streamlit Iris Flower Detector ML App </h2>
    </div> """

    st.markdown(html_temp, unsafe_allow_html=True)

    sepal_length = st.text_input("sepal_length", "Type Here")
    sepal_width = st.text_input("sepal_width", "Type Here")
    petal_length = st.text_input("petal_length", "Type Here")
    petal_width = st.text_input("petal_width", "Type Here")

    result = ""

    if st.button("Predict"):
        result = predict_flower(sepal_length, sepal_width, petal_length, petal_width)
    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__ == ' __main()__':
    main()