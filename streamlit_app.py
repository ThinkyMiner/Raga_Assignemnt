import streamlit as st
import sys
import os

# Add the root directory to the path so we can import from the app directory
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir)

# Import the streamlit app directly
from app.streamlit_app import *

# Add a footer note about GitHub repository
st.markdown("---")
st.markdown("View the full source code on [GitHub](https://github.com/ThinkyMiner/Raga_Assignemnt)")
st.markdown("Built by Kartik Sehgal")
