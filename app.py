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

def extract_article_text(soup):
    # Try different selectors for article content
    selectors = [
        'article',  # Common article tag
        '.article-content',  # Common class
        '.post-content',
        '.entry-content',
        '#content',
        'main',
        '.story-content'
    ]
    
    for selector in selectors:
        article = soup.select_one(selector)
        if article:
            return ' '.join([p.get_text() for p in article.find_all(['p', 'h1', 'h2', 'h3'])])
    
    # Fallback to all paragraphs if no specific selector works
    return ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])

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
        
        # Extract article text with improved method
        article_text = extract_article_text(soup)
        
        # Improved name extraction patterns
        name_patterns = [
            # Standard patterns
            (r'([A-Z][a-z]+ [A-Z][a-z]+), ([A-Z][a-zA-Z\s]+) of ([A-Z][a-zA-Z\s]+)', 3),  # Name, Role of Company
            (r'([A-Z][a-z]+ [A-Z][a-z]+), ([A-Z][a-zA-Z\s]+)', 2),  # Name, Role
            (r'([A-Z][a-z]+ [A-Z][a-z]+) of ([A-Z][a-zA-Z\s]+)', 2),  # Name of Company
            
            # Quoted patterns
            (r'"([A-Z][a-z]+ [A-Z][a-z]+)"', 1),  # "Name"
            (r'([A-Z][a-z]+ [A-Z][a-z]+) said', 1),  # Name said
            (r'([A-Z][a-z]+ [A-Z][a-z]+) told', 1),  # Name told
            
            # Role-based patterns
            (r'([A-Z][a-zA-Z\s]+) ([A-Z][a-z]+ [A-Z][a-z]+)', 2),  # Role Name
            (r'([A-Z][a-z]+ [A-Z][a-z]+), who ([a-z]+) at ([A-Z][a-zA-Z\s]+)', 3),  # Name, who works at Company
            
            # Simple name patterns (as fallback)
            (r'([A-Z][a-z]+ [A-Z][a-z]+)', 1)  # Simple name
        ]
        
        profiles = []
        for pattern, expected_groups in name_patterns:
            matches = re.finditer(pattern[0], article_text)
            for match in matches:
                try:
                    groups = match.groups()
                    if len(groups) != expected_groups:
                        continue
                        
                    if expected_groups == 3:
                        if pattern[0] == name_patterns[0][0]:  # Name, Role of Company
                            name, role, company = groups
                        else:  # Name, who works at Company
                            name, role, company = groups
                    elif expected_groups == 2:
                        if pattern[0] == name_patterns[1][0]:  # Name, Role
                            name, role = groups
                            company = "Organization"
                        elif pattern[0] == name_patterns[2][0]:  # Name of Company
                            name, company = groups
                            role = "Representative"
                        else:  # Role Name
                            role, name = groups
                            company = "Organization"
                    else:  # expected_groups == 1
                        name = groups[0]
                        role = "Expert"
                        company = "Organization"
                    
                    # Skip if it's likely a product name
                    if is_product_name(name):
                        continue
                    
                    # Find a quote associated with this person
                    quote_pattern = f'{name}[^.!?]*[.!?]'
                    quote_match = re.search(quote_pattern, article_text)
                    quote = quote_match.group(0) if quote_match else "No direct quote found"
                    
                    # Calculate confidence based on pattern match
                    confidence = 95 if expected_groups > 1 else 85
                    
                    profiles.append({
                        "name": name.strip(),
                        "role": role.strip(),
                        "company": company.strip(),
                        "quote": quote.strip(),
                        "confidence": confidence
                    })
                except Exception as e:
                    continue
        
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
