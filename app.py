import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

# Set page config
st.set_page_config(
    page_title="NewsNex - Turning Headlines into Human Intelligence",
    page_icon="📰",
    layout="wide"
)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def extract_profiles_from_article(url):
    try:
        # Validate URL
        if not is_valid_url(url):
            return None, "Invalid URL format. Please enter a valid news article URL."
        
        # Fetch the article
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract article text
        article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        # Basic name extraction (this is a simplified version)
        # In a real implementation, you would use NLP to identify people and their roles
        names = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', article_text)
        
        # Create mock profiles (replace this with your actual profile extraction logic)
        profiles = []
        for name in set(names[:5]):  # Limit to 5 unique names for demo
            profiles.append({
                "name": name,
                "role": "Expert",  # Replace with actual role extraction
                "company": "Organization",  # Replace with actual company extraction
                "quote": "Quote from article",  # Replace with actual quote extraction
                "confidence": 85  # Replace with actual confidence score
            })
        
        return profiles, None
        
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching the article: {str(e)}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

def main():
    st.title("📰 NewsNex - Turning Headlines into Human Intelligence")
    st.markdown("Extract key decision-makers and experts from news articles")
    
    # Input section
    url = st.text_input("Enter article URL", placeholder="https://example.com/article")
    
    if st.button("Extract Profiles"):
        if url:
            with st.spinner("Extracting profiles..."):
                profiles, error = extract_profiles_from_article(url)
                
                if error:
                    st.error(error)
                elif not profiles:
                    st.warning("No profiles found in this article. Please try another news article.")
                else:
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
