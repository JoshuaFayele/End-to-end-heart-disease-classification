# Basics & Fundamentals

# Core Packages
import streamlit as st

# st.title("My Streamlit Learning File")


# # Working with and Displaying Text
# st.text("Hello World, this is a text")
# name = "Joshua"
# st.text("My name is {}".format(name))

# # Title
# st.title("This is a title")

# # Header
# st.header("This is a header")

# # Subheader
# st.subheader("This is a subheader")

# # Markdown
# st.markdown("This is a markdown")


# # Displaying Coloured Text/Bootstraps Alert
# st.success("Successful")
# st.warning("Warning")
# st.info("This is an information")
# st.error("This is an error")
# st.exception("This is an exception")


# # Superfunction
# st.write("This is a normal text") # Text
# st.write("## This is a markdown text") # Markdown
# st.write(1+2) # Math function

# st.write(dir(st))

# # Help Info
# st.help(range)

# # Load EDA Packages
# import pandas as pd

# # Display Data
# df = pd.read_csv("D:\Downloads\iris.csv")

# # Method 1
# #st.dataframe(df)

# # Add height
# #st.dataframe(df, 2000, 500)

# # Adding a colour style from pandas
# #st.dataframe(df.style.highlight_max(axis=0))

# # Method 2: Static Table
# #st.table(df)

# # Method 3: Using superfunction 'st.write'
# st.write(df.head())

# # Display Json
# st.json({'data':'name'})

# # Display Code
# mycode = """
# def sayhello():
#     print("Hello Streamlit Universe")
# """
# st.code(mycode, language='python')

# # Working with Widgets
# # Buttons/Radio?Checkbox/Select/

# # Working with Buttons
# last_name = "Fayele"
# first_name = "Joshua"
# if st.button("Submit"):
#     st.write("Last Name: {}".format(last_name.upper()))

# if st.button("Submit", key='new1'):
#     st.write("First Name: {}".format(first_name.title()))

# # Working with RadioButtons
# status = st.radio("What us your status", ("Active", "Inactive"))
# if status == 'Active':
#     st.success("You are active")
# elif status == "Inactive":
#     st.warning("Inactive")
    
# # Working with Checkbox
# if st.checkbox("Show/Hide"):
#     st.text("Showing something")

# # Working with Beta Expander
# if st.expander("Python"):
#    st.success("Hello Python")

# with st.expander(label="Julia"):
#     st.text("Hello Julia")

# Select?Multiple select
my_lang = ["Python", "Julia", "Go", "Rust"]

choice = st.selectbox("Language", my_lang)
st.write("You selected {}".format(choice))

# Multiple Selection
spoken_lang = ("English", "French", "Spanish", "Twi")
my_spoken_lang = st.multiselect("Spoken Language", spoken_lang, default="English")

# Slider
# Numbers (Int/Float/Dates)
age = st.slider("Age", 1, 100)

# Any Datatype
# Select Slider
colour = st.select_slider("Choose Colour", options=["yellow", "red", "blue", "black", "white"], value=("yellow", "red"))

# Working with Media Files (videos/images/audio)
# Display Images
# from PIL import Image
# img = Image.open("D:\Downloads\data\image_03.jpg")
# st.image(img,use_column_width=True)

# # From URL
# st.image("https://th.bing.com/th/id/OIP.TYRKmRLMGM3TQMjEg3dc1AHaJQ?pid=ImgDet&rs=1")

# Display Videos
video_file = open("D:\Downloads\data\secret_of_success.mp4", "rb").read()
st.video(video_file, start_time=3)

# video_file1 = open("D:\Little Italy (2018)\Little Italy (2018) 1080p WEBRip [xPau.se].mp4", "rb").read()
# st.video(video_file1)

# Display Audio/Working with Audio
audio_file = open("D:\Downloads\data\song.mp3", "rb")
st.audio(audio_file.read(), format='audio/mp3')

