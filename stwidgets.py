import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")


if name :
    st.write(f"Hello, {name} How can I help you?")

age = st.slider("Select your age:",0,100,25)

st.write(f" Hi {name} your age is {age}.")

options = ["Python","Java","C++"]

choice = st.selectbox("Please select your favorite programming language: ", options)
st.write(f" Hi {name} , Your favorite language is {choice}.")


data = {
    "Name": ["Malik","Aqsa","Hamza","Laiba"],
    "Age" : [20,21,24,25],
    "City" : ["Karachi","Lahore","Multan","Sargodha"]
}

df = pd.DataFrame(data)

df.to_csv("sampledata.csv")

st.write(df)


uploaded_file = st.file_uploader("Choose a CSV file",type="csv")


if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)
    st.write(df)