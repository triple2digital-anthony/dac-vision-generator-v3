# DAC Vision Advanced Code Generator (Blue, Black, & Red Caps)

A sophisticated Streamlit application for generating DataMatrix codes that follow specific patterns for blue, black, and red polishing caps. This tool analyzes and generates codes that match the structural and statistical patterns observed in authentic samples.

## Features

- Generate random or sequential DataMatrix codes for:
  - Blue Caps
  - Black Caps
  - Red Caps
- Pattern-aware code generation following observed distributions
- Built-in validation and checksum verification
- Secure access with password protection
- Admin interface for access logging
- Dark/light mode support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/triple2digital-anthony/dac-vision-generator-v3.git
cd dac-vision-generator-v3
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run datamatrix_generator/main.py
```

2. Access the application:
- Main interface: http://localhost:8501
- Admin interface: http://localhost:8501/?page=admin

3. Enter the provided password to access the application.

## Code Generation Features

### Blue Caps
- Primarily start with "7" (50%), "v" (37.8%), or "65" (12.2%)
- Common prefix patterns: "65e", "65f", "65g", "736", "737", "738", "vxp", "vxq"
- Higher ratio of letters to numbers in middle segments

### Black Caps
- Primarily start with "7" (50%), "v" (37.8%), or "6" (12.2%)
- Common prefix patterns: "72c", "7c8", "7c9", "7de", "vcy", "vdn", "vdr"
- Balanced ratio of letters to numbers

### Red Caps
- Primarily start with "7" (50%), "v" (37.8%), or "64" (12.2%)
- Common prefix patterns: "72e", "72f", "72g", "v8n", "v8p", "v9w"
- Higher ratio of numbers to letters in middle segments

## Security Features

- Password-protected access
- Admin interface for access logging
- Secure code generation algorithms
- Input validation and sanitization

## Legal Disclaimer

This tool is provided for educational and research purposes only. The generated codes are based on observed patterns and may not be accepted by actual machines. Use of this tool to attempt to circumvent commercial licensing systems or security mechanisms may violate applicable laws and is not the intended purpose of this software. 