from setuptools import setup, find_packages

setup(
    name="datamatrix_generator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.30.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
    ],
) 