from setuptools import setup, find_packages

setup(
    name="newsnex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.32.0",
        "pandas==2.2.0",
        "numpy==1.26.4",
        "requests==2.31.0",
        "beautifulsoup4==4.12.3",
        "python-dotenv==1.0.1"
    ],
    python_requires=">=3.12",
    author="Your Name",
    author_email="your.email@example.com",
    description="NewsNex - AI-powered news article profile extraction",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/newsnex",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
    ],
) 
