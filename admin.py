"""
Admin page for the DataMatrix Code Generator application.
This page should be accessed directly via URL and is not visible from the main interface.
"""

import streamlit as st
import pandas as pd
from datamatrix_generator.utils.logger import AccessLogger

def main():
    st.set_page_config(
        page_title="Admin - DAC Generator",
        page_icon="🔒",
        layout="wide"
    )
    
    st.title("Admin Access Logs")
    
    # Password input for admin access
    admin_password = st.text_input("Enter admin password", type="password")
    
    if st.button("View Logs"):
        if admin_password == "dacvisaps41!":  # Using the same password as main app
            logger = AccessLogger()
            logs = logger.get_logs(admin_password)
            
            if logs:
                # Convert logs to DataFrame
                df = pd.DataFrame(logs)
                
                # Display logs in a table
                st.dataframe(df)
                
                # Add download button
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Logs as CSV",
                    data=csv,
                    file_name="access_logs.csv",
                    mime="text/csv"
                )
            else:
                st.info("No logs available.")
        else:
            st.error("Invalid admin password.")

if __name__ == "__main__":
    main() 