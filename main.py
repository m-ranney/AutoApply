import streamlit as st
from src.resume_processing import process_resume

def main():

    st.title("Resume Analyzer")

    uploaded_file = st.file_uploader("Upload your resume", type=['pdf'])

    if uploaded_file is not None:
        # Load the file using Langchain and process the resume.
        process_resume(uploaded_file)

    if st.button('Process'):
        # Here you can call the function that uses the processed resume for further steps
        pass

if __name__ == "__main__":
    main()
