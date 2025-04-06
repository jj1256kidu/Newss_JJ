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

def clean_text(text):
    # Remove extra whitespace and normalize newlines
    text = ' '.join(text.split())
    return text.strip()

def is_content_element(elem):
    # Skip elements that are likely navigation or non-content
    skip_classes = [
        'nav', 'navigation', 'menu', 'sidebar', 'ad', 'advertisement',
        'header', 'footer', 'top-bar', 'bottom-bar', 'social-share',
        'related', 'recommended', 'comments', 'newsletter', 'subscribe',
        'cookie', 'privacy', 'terms', 'language', 'edition'
    ]
    
    skip_ids = [
        'nav', 'menu', 'sidebar', 'header', 'footer', 'comments',
        'related', 'recommended', 'newsletter', 'subscribe'
    ]
    
    # Check element's class
    elem_classes = elem.get('class', [])
    if any(skip in ' '.join(elem_classes).lower() for skip in skip_classes):
        return False
    
    # Check element's id
    elem_id = elem.get('id', '')
    if any(skip in elem_id.lower() for skip in skip_ids):
        return False
    
    # Check element's role
    elem_role = elem.get('role', '')
    if elem_role in ['navigation', 'complementary', 'banner']:
        return False
    
    return True

def extract_article_text(soup):
    # Remove script and style elements
    for script in soup(["script", "style", "nav", "header", "footer"]):
        script.decompose()
    
    # Common article content selectors
    content_selectors = [
        'article',  # Common article tag
        '.article-content',
        '.post-content',
        '.entry-content',
        '#content',
        'main',
        '.story-content',
        '.article-body',
        '.article-text',
        '.article-main',
        '.article-wrapper',
        '.article-container',
        '.article-inner',
        '.article-detail',
        '.article-page',
        '.article-full'
    ]
    
    # Try to find the main content using selectors
    for selector in content_selectors:
        article = soup.select_one(selector)
        if article:
            # Get all text elements
            text_elements = article.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            # Filter out non-content elements
            text_elements = [elem for elem in text_elements if is_content_element(elem)]
            if text_elements:
                return clean_text(' '.join(elem.get_text() for elem in text_elements))
    
    # If no specific selector works, try to find the main content area
    main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=lambda x: x and 'content' in x.lower())
    if main_content:
        text_elements = main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        text_elements = [elem for elem in text_elements if is_content_element(elem)]
        if text_elements:
            return clean_text(' '.join(elem.get_text() for elem in text_elements))
    
    # Fallback to all paragraphs and headings
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    text_elements = [elem for elem in text_elements if is_content_element(elem)]
    return clean_text(' '.join(elem.get_text() for elem in text_elements))

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
