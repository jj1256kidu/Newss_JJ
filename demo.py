import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse
import re

# Set page config
st.set_page_config(
    page_title="NewsNex Demo",
    page_icon="📰",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .profile-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .confidence-badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        margin-left: 10px;
    }
    .high-confidence {
        background-color: #4CAF50;
        color: white;
    }
    .medium-confidence {
        background-color: #FFC107;
        color: black;
    }
    .low-confidence {
        background-color: #F44336;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def clean_text(text):
    return ' '.join(text.split())

def extract_profiles(text):
    # This is a simplified version - in production, you'd use more sophisticated NLP
    profiles = []
    
    # Pattern for finding names and titles
    name_pattern = r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)'  # Matches capitalized words
    title_pattern = r'(?:CEO|CTO|CFO|COO|Founder|Director|Manager|Head|Lead|President|Vice President|VP)'
    
    # Split text into sentences
    sentences = re.split(r'[.!?]', text)
    
    for sentence in sentences:
        # Look for names
        names = re.findall(name_pattern, sentence)
        for name in names:
            # Look for titles near the name
            title_match = re.search(title_pattern, sentence)
            title = title_match.group(0) if title_match else "Unknown"
            
            # Look for company mentions
            company_pattern = r'at\s+([A-Z][a-zA-Z\s]+(?:Inc\.|LLC|Ltd\.|Corp\.|Company)?)'
            company_match = re.search(company_pattern, sentence)
            company = company_match.group(1) if company_match else "Unknown"
            
            # Calculate confidence score (simplified)
            confidence = 0.7 if title != "Unknown" else 0.5
            confidence = 0.9 if company != "Unknown" else confidence
            
            profiles.append({
                "name": name,
                "title": title,
                "company": company,
                "context": clean_text(sentence),
                "confidence": confidence
            })
    
    return profiles

def main():
    st.title("📰 NewsNex Demo")
    st.markdown("### Extract Profiles from News Articles")
    
    # Input section
    col1, col2 = st.columns([3, 1])
    with col1:
        url = st.text_input("Enter news article URL", placeholder="https://example.com/article")
    with col2:
        st.markdown("### ")
        extract_button = st.button("Extract Profiles")
    
    if extract_button and url:
        with st.spinner("Analyzing article..."):
            try:
                # Validate URL
                if not is_valid_url(url):
                    st.error("Please enter a valid URL")
                    return
                
                # Fetch article
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                # Parse content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove unwanted elements
                for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                    element.decompose()
                
                # Get main content
                article_text = soup.get_text()
                article_text = clean_text(article_text)
                
                # Extract profiles
                profiles = extract_profiles(article_text)
                
                if profiles:
                    st.success(f"Found {len(profiles)} profiles!")
                    
                    # Display profiles
                    for profile in profiles:
                        with st.container():
                            st.markdown(f"""
                            <div class="profile-card">
                                <h3>{profile['name']}</h3>
                                <p><strong>Title:</strong> {profile['title']}</p>
                                <p><strong>Company:</strong> {profile['company']}</p>
                                <p><strong>Context:</strong> {profile['context']}</p>
                                <span class="confidence-badge {'high-confidence' if profile['confidence'] > 0.8 else 'medium-confidence' if profile['confidence'] > 0.6 else 'low-confidence'}">
                                    Confidence: {int(profile['confidence'] * 100)}%
                                </span>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    # Export options
                    st.markdown("### Export Options")
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("Download as CSV"):
                            df = pd.DataFrame(profiles)
                            csv = df.to_csv(index=False)
                            st.download_button(
                                label="Download CSV",
                                data=csv,
                                file_name="profiles.csv",
                                mime="text/csv"
                            )
                    
                    with col2:
                        if st.button("Download as JSON"):
                            import json
                            json_data = json.dumps(profiles, indent=2)
                            st.download_button(
                                label="Download JSON",
                                data=json_data,
                                file_name="profiles.json",
                                mime="application/json"
                            )
                else:
                    st.warning("No profiles found in the article. Try another URL.")
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching the article: {str(e)}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 
