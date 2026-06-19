import streamlit as st
import requests
st.title(" AI SDLC Engineer")
requirement=st.text_area("Enter your requirement")
if st.button("Generate"):
    response = requests.post("http://localhost:8000/generate")
    st.write(response.json())