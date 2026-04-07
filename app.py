import streamlit as st
from langgraph_workflow import run_validation_pipeline

st.title("🚀 Luca Validator")

if st.button("Run Validation"):
    result = run_validation_pipeline()
    st.write(result)