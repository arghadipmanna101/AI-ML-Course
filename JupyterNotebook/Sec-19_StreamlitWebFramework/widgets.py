import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name :")

if name:
    st.write(f"Hello, {name}")
    
age=st.slider("Select your age :",0,100,18)
st.write(f"Your age is : {age}.")

options=["Python","Java","C++","C","JavaScript"]
choice=st.selectbox("Chose your favorite language :",options)
st.write(f"Your fevarite coding language {choice}")


data={
    "Name":["John", "Jane","Jake","jill"],
    "Age": [28,24,35,40],
    "City": ["New York", "Los Angeles","Chicago","Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

# Uploade a file

uploader_file=st.file_uploader("Chose a CSV file.",type="csv")
if uploader_file is not None:
    df=pd.read_csv(uploader_file)
    st.write(df)