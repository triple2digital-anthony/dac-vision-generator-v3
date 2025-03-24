"""
Utility functions for the DataMatrix Code Generator application.
"""

from typing import List

def format_results(codes: List[str], cap_type: str = 'blue') -> str:
    """
    Format a list of codes into a string with proper formatting and background colors.
    
    Args:
        codes (List[str]): List of generated codes
        cap_type (str): Type of cap ('blue', 'black', or 'red')
        
    Returns:
        str: Formatted string of codes with HTML styling
    """
    # Define background colors for each cap type (25% darker than before)
    colors = {
        'blue': '#99ccff',  # Darker blue
        'black': '#cccccc',  # Darker gray
        'red': '#ff9999'    # Darker red
    }
    
    # Get the appropriate background color
    bg_color = colors.get(cap_type, '#ffffff')  # Default to white if cap_type not found
    
    # Format each code with background color and black text
    formatted_codes = []
    for i, code in enumerate(codes):
        formatted_code = f'<div style="background-color: {bg_color}; color: #000000; padding: 8px; margin: 4px 0; border-radius: 4px; font-family: monospace;">{i+1}. {code}</div>'
        formatted_codes.append(formatted_code)
    
    return "\n".join(formatted_codes) 