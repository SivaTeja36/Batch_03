import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, elements):
    """
    Scrape a website for specific HTML elements
    :param url: URL to scrape
    :param elements: Dictionary of elements to scrape {'element': 'css_class'}
    :return: Dictionary with scraped data or error message
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = {}
        
        for name, selector in elements.items():
            items = soup.select(selector)
            results[name] = [item.get_text(strip=True) for item in items]
            
        # Create DataFrame for easy export
        df = pd.DataFrame.from_dict(results, orient='index').transpose()
        
        return {
            'status': 'success',
            'data': results,
            'dataframe': df,
            'url': url
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'status': 'error',
            'message': f"Request failed: {str(e)}"
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f"An error occurred: {str(e)}"
        }