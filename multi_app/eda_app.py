import streamlit as st

# Load EDA Packages
import pandas as pd

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = pd.read_csv("C:\Users\USER\Projects\My-Streamlit-Learning-Notebook\multi_app\data\diabetes_data_upload.csv")
    st.dataframe(df)