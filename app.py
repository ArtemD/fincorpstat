import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

hide_streamlit_style = """
<style>
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title('Hello world!')