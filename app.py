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

def is_product_name(name):
    # List of common product-related terms to filter out
    product_terms = ['ultra', 'pro', 'max', 'plus', 'galaxy', 'note', 'edge', 'fold', 
                    'motorola', 'samsung', 'infinix', 'iphone', 'android', 'ios']
    return any(term in name.lower() for term in product_terms)

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
        
        # Improved name extraction
        # Look for patterns like "John Smith, CEO of Company" or "According to John Smith"
        name_patterns = [
            r'([A-Z][a-z]+ [A-Z][a-z]+), ([A-Z][a-zA-Z\s]+) of ([A-Z][a-zA-Z\s]+)',
            r'According to ([A-Z][a-z]+ [A-Z][a-z]+)',
            r'([A-Z][a-z]+ [A-Z][a-z]+), who ([a-z]+) at ([A-Z][a-zA-Z\s]+)',
            r'([A-Z][a-z]+ [A-Z][a-z]+), ([A-Z][a-zA-Z\s]+)'
        ]
        
        profiles = []
        for pattern in name_patterns:
            matches = re.finditer(pattern, article_text)
            for match in matches:
                if pattern == name_patterns[0]:  # "Name, Role of Company"
                    name, role, company = match.groups()
                elif pattern == name_patterns[1]:  # "According to Name"
                    name = match.group(1)
                    role = "Expert"
                    company = "Organization"
                elif pattern == name_patterns[2]:  # "Name, who works at Company"
                    name, role, company = match.groups()
                else:  # "Name, Role"
                    name, role = match.groups()
                    company = "Organization"
                
                # Skip if it's likely a product name
                if is_product_name(name):
                    continue
                
                # Find a quote associated with this person
                quote_pattern = f'{name}[^.!?]*[.!?]'
                quote_match = re.search(quote_pattern, article_text)
                quote = quote_match.group(0) if quote_match else "No direct quote found"
                
                profiles.append({
                    "name": name.strip(),
                    "role": role.strip(),
                    "company": company.strip(),
                    "quote": quote.strip(),
                    "confidence": 90  # Higher confidence for structured matches
                })
        
        # Remove duplicates while preserving order
        seen = set()
        unique_profiles = []
        for profile in profiles:
            if profile['name'] not in seen:
                seen.add(profile['name'])
                unique_profiles.append(profile)
        
        return unique_profiles, None
        
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
