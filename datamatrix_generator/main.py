"""
Main entry point for the DataMatrix Code Generator application.
"""

import streamlit as st
import pandas as pd
from datamatrix_generator.generator.datamatrix import DataMatrixCodeGenerator
from datamatrix_generator.ui.auth import check_password
from datamatrix_generator.ui.components import create_tab_ui, create_about_tab
from datamatrix_generator.utils.logger import AccessLogger

def create_admin_view():
    """Create the admin view for accessing logs."""
    st.title("Admin Access Logs")
    
    # Password input for admin access
    admin_password = st.text_input("Enter admin password", type="password")
    
    if st.button("View Logs"):
        if admin_password == "FG3bI<r3,3D7.~}y=g<0V":  # Admin password
            logger = AccessLogger()
            logs = logger.get_logs(admin_password)
            
            if logs:
                # Convert logs to DataFrame
                df = pd.DataFrame(logs)
                
                # Extract location info
                df['environment'] = df['location'].apply(lambda x: x.get('environment', 'Unknown'))
                df['type'] = df['location'].apply(lambda x: x.get('type', 'Unknown'))
                
                # Drop the original location column and reorder
                df = df.drop('location', axis=1)
                df = df[['timestamp', 'ip_address', 'user_agent', 'environment', 'type']]
                
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

def main():
    st.set_page_config(
        page_title="DAC Vision Advanced Code Generator (Blue, Black, & Red Caps)",
        page_icon="🔢",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Check if we're on the admin page
    is_admin = "page" in st.query_params and st.query_params["page"] == "admin"
    
    # Handle admin page separately
    if is_admin:
        create_admin_view()
        return
    
    # Regular app interface with password protection
    if check_password():
        # Initialize the generator if not already done
        if 'generator' not in st.session_state:
            st.session_state.generator = DataMatrixCodeGenerator()
        
        # Page header
        st.title("DAC Vision Advanced Code Generator (Blue, Black, & Red Caps)")
        st.write("Generate codes that follow the patterns identified in the blue, black, and red cap sample datasets.")
        
        # Create tabs for different cap types and about section
        tab1, tab2, tab3, tab4 = st.tabs(["🔵 Blue Cap", "⚫ Black Cap", "🔴 Red Cap", "ℹ️ About"])
        
        with tab1:
            create_tab_ui("blue")
        with tab2:
            create_tab_ui("black")
        with tab3:
            create_tab_ui("red")
        with tab4:
            create_about_tab()

if __name__ == "__main__":
    main() 