import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Doraemon App", layout="centered")

st.title("Hello, Poulabi! :heartpulse:")
st.write(":streamlit: Welcome to the Streamlit app.")
st.text("😎 Let's get started")

# Conditional logic with widgets
name = st.text_input("Enter your name:👻")
if st.button("Click Me!"):
    st.success(f"Hello, {name}! :wave:")

# Sidebar
st.sidebar.title("Navigation")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")
st.video("https://youtu.be/mimoQBL0u5w?si=UrfoJuYrOweKs_up")

# File uploading
uploaded_file = st.sidebar.file_uploader("Upload a file", type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Main content
st.title("Welcome to Doraemon's World! :sparkles:")
st.header("Watch Doraemon on Disney Channel")
st.markdown("**Bold**, *Italic*, and `Code`, [Link](https://www.streamlit.io/)")
st.code("print('Hello, Doraemon!')", language='python')

st.text_input("Enter your favorite Doraemon gadget:")
st.text_area("Describe your favorite Doraemon gadget:")
st.number_input("Enter a number related to Doraemon", min_value=0, max_value=100, value=50)
st.slider("Select a value related to Doraemon:", 0, 100, 50)
st.selectbox("Choose your favorite Doraemon character:", ["Doraemon", "Nobita", "Shizuka", "Gian", "Suneo"])
st.multiselect("Select multiple Doraemon characters:", ["Doraemon", "Nobita", "Shizuka", "Gian", "Suneo"])
st.radio("Choose your favorite Doraemon gadget:", ["Take-copter", "Anywhere Door", "Time Machine"])
st.checkbox("I love Doraemon!")

if st.button("Click Doraemon Gadgets"):
    st.success("Doraemon's gadgets are amazing! :sparkles:")

if st.checkbox("Show Doraemon's gadgets"):
    st.info("Here are some of Doraemon's gadgets: Take-copter, Anywhere Door, Time Machine, Bamboo Copter, and more! :rocket:")

# Login form
with st.form("Login Form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")
    if submit_button:
        st.success(f"Welcome, {username}! You are now logged in. :tada:")

# Columns
col1, col2 = st.columns(2)
with col1:
    st.button("Press me in column 1!")
with col2:
    st.button("Press me in column 2!")

# ✅ Safely handle audio playback
if os.path.exists("example.mp3"):
    with open("example.mp3", "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
else:
    st.warning("Audio file 'example.mp3' not found!")

# Matplotlib plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)

# Plotly chart
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Iris Dataset Scatter Plot')
st.plotly_chart(fig)

