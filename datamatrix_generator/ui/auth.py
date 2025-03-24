"""
Authentication module for the DataMatrix Code Generator application.
"""

import streamlit as st
from datamatrix_generator.utils.logger import AccessLogger

def check_password():
    """
    Returns True if the user entered the correct password.
    """
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "dacvisaps41!":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False
            st.session_state["show_error"] = True

    # First run or password not correct yet
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
        st.session_state["show_error"] = False
        # Log access attempt with basic info
        logger = AccessLogger()
        logger.log_access(
            ip_address="Local Access",  # Simplified for now
            user_agent="Streamlit App"  # Simplified user agent
        )

    if not st.session_state["password_correct"]:
        # Create the password input box and submit button
        st.markdown("""
        <style>
        .stApp {
            background-color: #1a1a1a !important;
        }
        div[data-testid="stVerticalBlock"] {
            background-color: #2d2d2d;
            padding: 3rem;
            border-radius: 10px;
            max-width: 500px;
            margin: 100px auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        .title-text {
            font-size: 3.5rem !important;
            font-weight: 700 !important;
            margin-bottom: 2rem !important;
            color: white !important;
        }
        .subtitle-text {
            font-size: 1.2rem !important;
            color: #cccccc !important;
            margin-bottom: 4rem !important;
        }
        div[data-testid="stTextInput"] > div > div {
            background-color: #1a1a1a !important;
            color: white !important;
            border: none !important;
            padding: 0.75rem !important;
            border-radius: 4px !important;
            font-size: 1.1rem !important;
        }
        div.stButton > button {
            background-color: #f85a5a !important;
            color: white !important;
            border: none !important;
            padding: 0.5rem 2rem !important;
            font-size: 1.2rem !important;
            width: 100% !important;
            margin-top: 0.5rem !important;
            letter-spacing: 0.2rem !important;
        }
        div.stButton > button:hover {
            background-color: #ff6b6b !important;
        }
        div[data-testid="stAlert"] {
            background-color: rgba(255, 76, 76, 0.2) !important;
            border-color: #ff4c4c !important;
            color: white !important;
            margin-bottom: 1rem !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="title-text">DAC Generator</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-text">Please enter the password to access the application.</p>', unsafe_allow_html=True)
        
        # Show error message if password was incorrect
        if st.session_state.get("show_error", False):
            st.error("Incorrect password. Please try again.")
            st.session_state["show_error"] = False
        
        # Create a single column layout for vertical stacking
        st.text_input(
            "Enter password", 
            type="password", 
            key="password",
            placeholder="Enter password",
            label_visibility="collapsed"
        )
        
        st.button("Access", on_click=password_entered, type="primary")
        
        return False
    
    return True 