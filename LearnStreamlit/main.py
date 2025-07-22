import streamlit as st
import pandas as pd
import numpy as np

# Greeting
st.write("Hello Ritesh")

# Text input for favorite movie
x = st.text_input("Favourite Movie:-?")
st.text("Input is funny:- " + x)

# Read and display CSV file
data = pd.read_csv("Spells.csv")
st.write(data)

# Generate random data with 3 columns
char_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

# Display charts
st.bar_chart(char_data)
st.line_chart(char_data)


# Multipage


