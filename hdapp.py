import streamlit as st
import pandas as pd
import numpy as np

# Configure Streamlit page
from PIL import Image
img = Image.open("D:\Downloads\heart.png")
st.set_page_config(page_title='Heart Disease Prediction App', page_icon=img)

#st.set_page_config(layout="wide")
st.title("Heart Disease Prediction Application")
st.header("This application predicts if a patient has _heart disease_ from their given features")
name = "Joshua Fayele"
st.markdown("_This application is developed by Joshua Fayele_")

st.subheader("Heart Disease Table")
df = pd.read_csv("D:\Downloads\heart-disease.csv")
st.dataframe(df)

