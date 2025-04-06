import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

# Set page config
st.set_page_config(
    page_title="NewsNex - Turning Headlines into Human Intelligence",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #F9FAFB;
    }
    .profile-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .confidence-high {
        color: #10B981;
    }
    .confidence-medium {
        color: #F59E0B;
    }
    </style>
    """, unsafe_allow_html=True)

# Mock data for demonstration
MOCK_PROFILES = [
    {
        "id": 1,
        "name": "John Smith",
        "role": "CTO",
        "company": "TechCorp",
        "quote": "We're investing $100M in AI research to push the boundaries of what's possible in enterprise technology.",
        "confidence": 95,
        "linkedInUrl": "https://linkedin.com/in/johnsmith",
    },
    {
        "id": 2,
        "name": "Sarah Johnson",
        "role": "Head of AI Research",
        "company": "TechCorp",
        "quote": "This investment will accelerate our development of next-generation AI solutions for businesses.",
        "confidence": 88,
        "linkedInUrl": "https://linkedin.com/in/sarahjohnson",
    },
    {
        "id": 3,
        "name": "Michael Chen",
        "role": "VP of Engineering",
        "company": "TechCorp",
        "quote": "Our team is excited to lead the charge in developing cutting-edge AI technologies.",
        "confidence": 92,
        "linkedInUrl": "https://linkedin.com/in/michaelchen",
    }
]

def extract_profiles(url):
    """Mock function to extract profiles from a URL"""
    # In a real implementation, this would use NLP to extract profiles
    return MOCK_PROFILES

def display_profile_card(profile):
    """Display a profile card with all relevant information"""
    confidence_class = "confidence-high" if profile["confidence"] > 90 else "confidence-medium"
    
    st.markdown(f"""
    <div class="profile-card">
        <h3>👤 {profile['name']}</h3>
        <p>🏢 {profile['role']} at {profile['company']}</p>
        <p class="{confidence_class}">📊 Confidence: {profile['confidence']}%</p>
        <p>💬 "{profile['quote']}"</p>
        <a href="{profile['linkedInUrl']}" target="_blank">🔗 View LinkedIn Profile</a>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    st.sidebar.title("NewsNex")
    st.sidebar.markdown("---")
    
    # Main content
    st.title("📰 NewsNex - Turning Headlines into Human Intelligence")
    st.markdown("Extract key decision-makers and experts from news articles")
    
    # Input section
    col1, col2 = st.columns([3, 1])
    with col1:
        url = st.text_input("Enter article URL", placeholder="https://example.com/article")
    with col2:
        st.markdown("")
        st.markdown("")
        if st.button("Extract Profiles"):
            if url:
                with st.spinner("Extracting profiles..."):
                    profiles = extract_profiles(url)
                    st.success(f"Found {len(profiles)} profiles!")
                    
                    # Display profiles
                    for profile in profiles:
                        display_profile_card(profile)
                    
                    # Export options
                    st.markdown("### Export Options")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button("Export as CSV"):
                            df = pd.DataFrame(profiles)
                            st.download_button(
                                label="Download CSV",
                                data=df.to_csv(index=False),
                                file_name="profiles.csv",
                                mime="text/csv"
                            )
                    with col2:
                        if st.button("Export as JSON"):
                            st.download_button(
                                label="Download JSON",
                                data=json.dumps(profiles, indent=2),
                                file_name="profiles.json",
                                mime="application/json"
                            )
                    with col3:
                        if st.button("Generate Outreach"):
                            st.info("Outreach generation coming soon!")
            else:
                st.error("Please enter a valid URL")

    # Recent extractions
    st.markdown("### Recent Extractions")
    recent_data = pd.DataFrame([
        {"Title": "Tech Giant Announces Major AI Investment", "Profiles": 3, "Date": "2h ago"},
        {"Title": "Startup Raises $50M in Series B", "Profiles": 5, "Date": "4h ago"},
        {"Title": "Industry Leader Appoints New CTO", "Profiles": 2, "Date": "1d ago"}
    ])
    
    st.dataframe(
        recent_data,
        column_config={
            "Title": st.column_config.TextColumn("Article Title"),
            "Profiles": st.column_config.NumberColumn("Profiles Found"),
            "Date": st.column_config.TextColumn("Time Ago")
        },
        hide_index=True
    )

if __name__ == "__main__":
    main() 