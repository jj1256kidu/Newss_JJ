import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Set page config
st.set_page_config(
    page_title="NewsNex - Turning Headlines into Human Intelligence",
    page_icon="📰",
    layout="wide"
)

def main():
    st.title("📰 NewsNex - Turning Headlines into Human Intelligence")
    st.markdown("Extract key decision-makers and experts from news articles")
    
    # Input section
    url = st.text_input("Enter article URL", placeholder="https://example.com/article")
    
    if st.button("Extract Profiles"):
        if url:
            with st.spinner("Extracting profiles..."):
                try:
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
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter a valid URL")

if __name__ == "__main__":
    main()
