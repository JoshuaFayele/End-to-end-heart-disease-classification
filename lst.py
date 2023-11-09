# Basics & Fundamentals

# Core Packages
import streamlit as st

# Working with and Displaying Text
st.text("Hello World, this is a text")
name = "Joshua"
st.text("My name is {}".format(name))

# Title
st.title("This is a title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("This is a markdown")


# Displaying Coloured Text/Bootstraps Alert
st.success("Successful")
st.warning("Warning")
st.info("This is an information")
st.error("This is an error")
st.exception("This is an exception")


# Superfunction
st.write("This is a normal text") # Text
st.write("## This is a markdown text") # Markdown
st.write(1+2) # Math function

st.write(dir(st))

# Help Info
st.help(range)

# Load EDA Packages
import pandas as pd

# Display Data
df = pd.read_csv("D:\Downloads\iris.csv")

# Method 1
st.dataframe(df)