import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write("Type of Analysis")
selected_option = st.sidebar.radio(
    "Select one option", ["Line Graph", "Bar Graph", "Area Chart"]
)

data = pd.DataFrame(np.random.randn(50, 2), columns=["Age", "BMI"])

if selected_option == "Line Graph":
    st.write("Line Graph")
    st.line_chart(data)
    st.write("This is a line graph of Age and BMI")
elif selected_option == "Bar Graph":
    st.write("Bar Graph")
    st.bar_chart(data)
    st.write("This is a bar graph of Age and BMI")
elif selected_option == "Area Chart":
    st.write("Area Chart")
    st.area_chart(data)
    st.write("This is an area chart of Age and BMI")
else:
    st.write("Please select an option from the sidebar to see the graph.")
