import streamlit as st
import requests
import os

st.set_page_config(
    page_title="AI SDLC Engineer",
    layout="wide"
)

st.title(" AI SDLC Engineer")

requirement = st.text_area(
    "Enter Project Requirement",
    height=200
)

if st.button("Generate Project"):

    with st.spinner("Running AI SDLC Pipeline..."):

        response = requests.post(
            "http://localhost:8000/generate-project",
            json={
                "requirement": requirement
            }
        )

        result = response.json()

        st.success(
            "Project Generated Successfully"
        )

        st.subheader(
            "Requirement Analysis"
        )

        st.json(
            result["analysis"]
        )

        st.subheader(
            "Architecture"
        )

        st.json(
            result["architecture"]
        )

        st.subheader(
            "Project Specification"
        )

        st.json(
            result["spec"]
        )

        st.subheader(
            "Validation Result"
        )

        if result["issues"]:

            st.error(
                "Validation Issues Found"
            )

            st.json(
                result["issues"]
            )

        else:

            st.success(
                "No Validation Issues Found"
            )

        st.subheader(
            "Generated Files"
        )

        if os.path.exists(
            "generated_code"
        ):

            for root, dirs, files in os.walk(
                "generated_code"
            ):

                for file in files:

                    st.text(
                        os.path.join(
                            root,
                            file
                        )
                    )