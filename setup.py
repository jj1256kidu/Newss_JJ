from setuptools import setup, find_packages

setup(
    name="newsnex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.28.0",
        "pandas==2.0.3",
        "numpy==1.24.3",
        "requests==2.31.0",
        "beautifulsoup4==4.12.2",
        "python-dotenv==1.0.0",
        "protobuf==3.20.3",
        "typing-extensions==4.7.1",
        "packaging==23.1",
        "tenacity==8.2.2",
        "pyarrow==12.0.1",
        "tornado==6.3.2",
        "click==8.1.7",
        "rich==13.5.2",
        "plotly==5.17.0"
    ],
    python_requires=">=3.8",
) 
