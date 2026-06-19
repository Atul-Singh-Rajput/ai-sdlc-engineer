import streamlit as st
import requests
st.title(" AI SDLC Engineer")
requirement=st.text_area("Enter your requirement")
if st.button("Generate"):
    with st.spinner(
        "Analyzing Requirement....."
    ):
        response = requests.post("http://localhost:8000/analyze-requirement", 
                                 json={
                                     "requirement": requirement
                                    }
                                 )
        st.json(response.json())