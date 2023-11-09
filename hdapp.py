import streamlit as st
import pandas as pd
import numpy as np

#st.set_page_config(layout="wide")
st.title("Heart Disease Prediction Application")
st.header("This application predicts if a patient has _heart disease_ from their given features")

#df = pd.read_csv("C:\Users\USER\Projects\End-to-end-heart-disease-classification\heart-disease.csv")
#st.table(df)

#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

name = "Joshua Fayele"
st.text("This is application was developed by {}".format(name))