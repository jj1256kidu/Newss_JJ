import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Set page config
st.set_page_config(
    page_title="NewsNex - Article Text Extractor",
    page_icon="📰",
    layout="wide"
)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

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

def main():
    st.title("📰 NewsNex - Article Text Extractor")
    st.markdown("Extract text content from news articles")
    
    # Input section
    url = st.text_input("Enter article URL", placeholder="https://example.com/article")
    
    if st.button("Extract Text"):
        if url:
            with st.spinner("Extracting text..."):
                try:
                    # Validate URL
                    if not is_valid_url(url):
                        st.error("Invalid URL format. Please enter a valid news article URL.")
                        return
                    
                    # Fetch the article
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    }
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    
                    # Parse the content
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Extract article text
                    article_text = extract_article_text(soup)
                    
                    if article_text.strip():
                        st.success("Text extracted successfully!")
                        st.markdown("### Article Text")
                        st.text_area("", article_text, height=400)
                        
                        # Add download button
                        st.download_button(
                            label="Download Text",
                            data=article_text,
                            file_name="article_text.txt",
                            mime="text/plain"
                        )
                    else:
                        st.warning("No text content found in the article.")
                        
                except requests.exceptions.RequestException as e:
                    st.error(f"Error fetching the article: {str(e)}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter a valid URL")

if __name__ == "__main__":
    main()
