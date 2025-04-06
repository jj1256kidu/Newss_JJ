import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import logging
import sys
import traceback
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('newsnex.log')
    ]
)
logger = logging.getLogger('NewsNex')

# Set page config
st.set_page_config(
    page_title="NewsNex - Turning Headlines into Human Intelligence",
    page_icon="��",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #F9FAFB;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("📰 NewsNex - Turning Headlines into Human Intelligence")
    st.markdown("Extract key decision-makers and experts from news articles")
    
    # Input section
    url = st.text_input("Enter article URL", placeholder="https://example.com/article")
    
    if st.button("Extract Profiles"):
        if url:
            with st.spinner("Extracting profiles..."):
                # Mock data for demonstration
                profiles = [
                    {
                        "name": "John Smith",
                        "role": "CTO",
                        "company": "TechCorp",
                        "quote": "We're investing in AI research.",
                        "confidence": 95
                    },
                    {
                        "name": "Sarah Johnson",
                        "role": "Head of AI Research",
                        "company": "TechCorp",
                        "quote": "This investment will accelerate development.",
                        "confidence": 88
                    }
                ]
                
                st.success(f"Found {len(profiles)} profiles!")
                
                # Display profiles
                for profile in profiles:
                    st.markdown(f"""
                    <div style='background-color: white; padding: 20px; border-radius: 12px; margin: 10px 0;'>
                        <h3>👤 {profile['name']}</h3>
                        <p>🏢 {profile['role']} at {profile['company']}</p>
                        <p>💬 "{profile['quote']}"</p>
                        <p>📊 Confidence: {profile['confidence']}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Export options
                if st.button("Export as CSV"):
                    df = pd.DataFrame(profiles)
                    st.download_button(
                        label="Download CSV",
                        data=df.to_csv(index=False),
                        file_name="profiles.csv",
                        mime="text/csv"
                    )
        else:
            st.error("Please enter a valid URL")

if __name__ == "__main__":
    main() 
