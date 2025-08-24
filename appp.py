import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import requests

# Title of the Application
st.title("Enhanced Streamlit Dashboard")

# Display a simple text
st.write("We are learning to develop a more powerful frontend using Streamlit")

# Sidebar Navigation
menu = st.sidebar.selectbox("Select Section", ["Home", "DataFrame", "Charts", "Excel Upload", "API Data"])

# ----------------- Home -----------------
if menu == "Home":
    st.subheader("Welcome!")
    st.write("Use the sidebar to explore different features.")

# ----------------- DataFrame -----------------
elif menu == "DataFrame":
    st.subheader("Sample DataFrame")
    df = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50]
    })
    st.write("Here is the DataFrame")
    st.write(df)

# ----------------- Charts -----------------
elif menu == "Charts":
    st.subheader("Visualizations")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3), columns=['A', 'B', 'C']
    )
    
    # Line chart (Streamlit)
    st.line_chart(chart_data)

    # Matplotlib Chart
    st.write("Matplotlib Chart")
    fig, ax = plt.subplots()
    ax.plot(chart_data['A'], label='A')
    ax.plot(chart_data['B'], label='B')
    ax.plot(chart_data['C'], label='C')
    ax.legend()
    st.pyplot(fig)

    # Plotly Chart
    st.write("Plotly Interactive Chart")
    fig_plotly = px.line(chart_data, y=['A', 'B', 'C'], title="Interactive Line Chart")
    st.plotly_chart(fig_plotly)

# ----------------- Excel Upload -----------------
elif menu == "Excel Upload":
    st.subheader("Upload an Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    if uploaded_file is not None:
        df_excel = pd.read_excel(uploaded_file)
        st.write("Preview of Excel File")
        st.dataframe(df_excel)

# ----------------- API Data -----------------
elif menu == "API Data":
    st.subheader("Fetch API Data")
    st.write("Demo: Fetching data from JSONPlaceholder API")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        st.json(data[:5])  # show first 5 posts
    else:
        st.error("Failed to fetch API data")

