import streamlit as st
import pandas as pd
import numpy as np

#st.set_page_config(layout="wide")
st.title("Heart Disease Prediction Application")
st.header("This application predicts if a patient has _heart disease_ from their given features")
name = "Joshua Fayele"
st.markdown("_This application is developed by Joshua Fayele_")

st.subheader("Heart Disease Table")
df = pd.read_csv("D:\Downloads\heart-disease.csv")
st.dataframe(df)

