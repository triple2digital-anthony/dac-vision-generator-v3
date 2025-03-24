"""
Custom styles for the DataMatrix Code Generator application.
"""

import streamlit as st

def load_css() -> None:
    """Load custom CSS to match the original styling."""
    
    # Define CSS
    css = """
    <style>
        /* Code display styling */
        .stCodeBlock {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 0.5rem 0;
            transition: all 0.2s ease-in-out;
        }
        
        .stCodeBlock:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        /* Button styling */
        .stButton > button {
            transition: all 0.2s ease-in-out;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        /* Input styling */
        .stNumberInput > div > div > input {
            border-radius: 0.5rem;
            border: 1px solid rgba(0, 0, 0, 0.1);
            padding: 0.5rem;
        }
        
        .stSelectbox > div > div > select {
            border-radius: 0.5rem;
            border: 1px solid rgba(0, 0, 0, 0.1);
            padding: 0.5rem;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease-in-out;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px);
        }
        
        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            .stCodeBlock {
                background-color: rgba(255, 255, 255, 0.05);
            }
            
            .stNumberInput > div > div > input,
            .stSelectbox > div > div > select {
                background-color: rgba(255, 255, 255, 0.05);
                border-color: rgba(255, 255, 255, 0.1);
                color: white;
            }
        }
    </style>
    """
    
    # Apply CSS
    st.markdown(css, unsafe_allow_html=True) 