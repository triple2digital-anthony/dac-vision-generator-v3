"""
UI components for the DataMatrix Code Generator application.
"""

import streamlit as st
import pandas as pd
import time
from typing import List, Dict, Optional, Tuple

from datamatrix import DataMatrixCodeGenerator
from helpers import format_results
from logger import AccessLogger

def create_tab_ui(cap_type: str) -> None:
    """Create the UI for a specific cap type tab."""
    
    # Generate Sequential Codes section
    st.subheader("Generate Sequential Codes")
    col1, col2, col3 = st.columns(3)
    with col1:
        counter = st.number_input("Starting Counter", value=1, min_value=1, key=f"counter_{cap_type}")
    with col2:
        count = st.number_input("Count", value=10, min_value=1, max_value=1000, key=f"count_{cap_type}")
    with col3:
        prefix_type = st.selectbox(
            "Prefix Type",
            options=[
                "7 (50%)",
                "v (37.8%)",
                "6 (12.2%)"
            ],
            key=f"prefix_{cap_type}"
        )
        prefix_value = prefix_type.split()[0]
    
    if st.button("Generate Sequential Codes", key=f"seq_{cap_type}"):
        generate_sequential(counter, count, prefix_value, cap_type)
    
    # Generate Random Codes section
    st.subheader("Generate Random Codes")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Generate 10 Random Codes", key=f"random10_{cap_type}"):
            generate_random(10, cap_type)
    with col2:
        if st.button(f"Generate 100 Random Codes", key=f"random100_{cap_type}"):
            generate_random(100, cap_type)

def show_generation_animation():
    """Show a fake AI processing animation for visual effect."""
    stages = [
        ("🧠 Contacting neural network", "#4c8bf5"),  # Blue
        ("🤖 Adapting Machine Learning", "#ff6b6b"),  # Red
        ("🎲 Markov Decision Process (MDP)", "#28a745"),  # Green
        ("🔄 Long Short-Term Memory Test", "#17a2b8"), # Cyan
        ("🎯 Convolutional Neural Networks", "#6f42c1"), # Purple
        ("✨ Success!", "#28a745")  # Green
    ]
    
    # Add some styling for the animation
    st.markdown("""
        <style>
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
        .stProgress > div > div {
            transition: width 0.3s ease-in-out;
        }
        .status-text {
            font-size: 1.1rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            animation: pulse 1.5s infinite;
        }
        </style>
    """, unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Calculate time per stage to total 2 seconds
    stage_time = 2.0 / len(stages)
    
    for idx, (stage, color) in enumerate(stages):
        progress = (idx + 1) / len(stages)
        # Create colored status text with animation
        status_html = f'<p class="status-text" style="color: {color};">{stage}</p>'
        status_text.markdown(status_html, unsafe_allow_html=True)
        progress_bar.progress(progress)
        time.sleep(stage_time)
    
    # Clean up the progress indicators
    time.sleep(0.3)  # Shorter pause at the end
    progress_bar.empty()
    status_text.empty()

def generate_random(count: int, cap_type: str) -> None:
    """Generate random codes and display them."""
    show_generation_animation()
    codes = st.session_state.generator.generate_random_batch(count)
    display_results(f"Generated {count} Random {cap_type.capitalize()} Cap Codes:", codes, cap_type)

def generate_sequential(start_counter: int, count: int, prefix_type: str, cap_type: str) -> None:
    """Generate sequential codes and display them."""
    show_generation_animation()
    codes = st.session_state.generator.generate_sequential_batch(start_counter, count, prefix_type)
    display_results(f"Generated {count} Sequential {cap_type.capitalize()} Cap Codes (starting at {start_counter}):", codes, cap_type)

def display_results(title: str, codes: List[str], cap_type: str) -> None:
    """Display generated codes with proper formatting."""
    st.subheader(title)
    
    # Display formatted results with background colors
    formatted_results = format_results(codes, cap_type)
    st.markdown(formatted_results, unsafe_allow_html=True)
    
    # Copy to clipboard functionality
    if codes:
        codes_text = "\n".join(codes)
        st.download_button(
            label="Download Codes as Text",
            data=codes_text,
            file_name=f"{cap_type}_codes.txt",
            mime="text/plain"
        )

def create_about_tab() -> None:
    """Create the About tab content."""
    st.title("About This Tool")

    # Purpose and Background
    st.header("Purpose and Background")
    st.write("""
    This tool analyzes and generates DataMatrix codes that follow patterns observed in Schneider Optical Machines' polishing caps. 
    These specialized caps are essential components in precision optical manufacturing equipment, used for polishing high-end lenses 
    and optical elements. Each cap incorporates a sophisticated one-time use security mechanism via DataMatrix codes to ensure 
    quality control and prevent unauthorized reuse.
    """)

    # Technical Analysis Methodology
    st.header("Technical Analysis Methodology")
    st.write("""
    Our research team conducted an extensive analysis of over 500 authentic polishing cap codes across all three color variants 
    (blue, black, and red). The analysis involved:
    """)
    st.markdown("""
    - Pattern recognition algorithms to identify consistent structures
    - Statistical analysis of character distributions
    - Validation testing against known authentic codes
    """)

    # Code Pattern Analysis
    st.header("Code Pattern Analysis")
    
    # General Characteristics
    st.subheader("General Characteristics")
    st.markdown("""
    - **Length**: All codes are exactly 26 characters long
    - **Character Set**: Codes use only lowercase letters (a-z) and numbers (0-9)
    - **Structure**: Each code consists of a prefix segment, a data segment, and a validation digit
    """)

    # Color-Specific Patterns
    st.subheader("Color-Specific Patterns")

    # Blue Caps
    st.markdown("**Blue Caps**")
    st.markdown("""
    - Primarily start with "7" (50%), "v" (37.8%), or "65" (12.2%)
    - Common prefix patterns include: "65e", "65f", "65g", "736", "737", "738", "vxp", "vxq"
    - Middle segments tend to have a higher ratio of letters to numbers (approximately 3:1)
    - More likely to contain characters from the middle of the alphabet (j-q)
    """)

    # Black Caps
    st.markdown("**Black Caps**")
    st.markdown("""
    - Primarily start with "7" (50%), "v" (37.8%), or "6" (12.2%)
    - Common prefix patterns include: "72c", "7c8", "7c9", "7de", "vcy", "vdn", "vdr"
    - Middle segments have a balanced ratio of letters to numbers (approximately 1:1)
    - More likely to contain characters from the beginning of the alphabet (a-i)
    """)

    # Red Caps
    st.markdown("**Red Caps**")
    st.markdown("""
    - Primarily start with "7" (50%), "v" (37.8%), or "64" (12.2%)
    - Common prefix patterns include: "72e", "72f", "72g", "v8n", "v8p", "v9w"
    - Middle segments tend to have a higher ratio of numbers to letters (approximately 3:2)
    - More likely to contain characters from the end of the alphabet (r-z)
    """)

    # Validation Mechanism
    st.subheader("Validation Mechanism")
    st.markdown("""
    - The last character is always an even digit (2, 4, 6, or 8)
    - This digit is calculated using a proprietary checksum algorithm based on the preceding 25 characters
    - The checksum appears to involve XOR operations on character values, ultimately producing a value 0-3 which maps to the corresponding even digit
    """)

    # Application Uses
    st.header("Application Uses")
    st.write("This tool can be valuable for:")
    st.markdown("""
    1. **Research and Development**: Studying security mechanisms in industrial equipment
    2. **Testing and Quality Assurance**: Creating test datasets for optical equipment validation
    3. **Legacy Equipment Maintenance**: Assisting with maintenance of older equipment where original caps may no longer be available
    """)

    # Technological Implementation
    st.header("Technological Implementation")
    st.write("The generator implements a sophisticated algorithm that:")
    st.markdown("""
    - Accurately models the statistical distribution of characters in authentic codes
    - Correctly implements the observed checksum algorithm
    - Produces codes that match the structural patterns of each color variant
    - Can generate both random codes and sequential series for testing purposes
    """)

    # Ethical Considerations
    st.header("Ethical Considerations")
    st.markdown("""
    The development of this tool raises important ethical considerations:
    - The research was conducted on publicly available data
    - All engineering was performed for educational and research purposes
    - The tool does not circumvent any DRM or security mechanisms
    - Generated codes are clearly marked as non-authentic and for educational use only
    """)

    # Legal Disclaimer
    st.header("Legal Disclaimer")
    st.write("""
    This tool is provided for educational and research purposes only. The generated codes are based on observed patterns 
    and may not be accepted by actual machines. Use of this tool to attempt to circumvent commercial licensing systems 
    or security mechanisms may violate applicable laws and is not the intended purpose of this software. All users bear 
    full responsibility for ensuring their use of this tool complies with all applicable laws and regulations.
    """)
    
    st.write("""
    Use at your own risk. The developers of this tool make no warranties or guarantees regarding its accuracy, reliability, 
    or suitability for any purpose.
    """) 