import streamlit as st
import pandas as pd
import numpy as np

## Title of the Application 

## important component
st.title("Hello Tecrix Students!")

## Display a simple text
st.write("We are learning to develop a frontend on Streamlit")

##create a simple DataFrame

df = pd.DataFrame({
    'col1' : [1,2,3,4,5],
    'col2' : [10,20,30,40,50]
})


# Display my DataFrame
st.write("Here is the Dataframe")
st.write(df)

## create  a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

