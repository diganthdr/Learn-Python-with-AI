"""
news.py
This module contains functions to scrape news headlines from the Times of India website.
"""
import requests
from bs4 import BeautifulSoup

def scrape_toi_headlines():
    """Scrape the latest headlines from Times of India."""

    url = "https://timesofindia.indiatimes.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    # Adjusted selector to fetch actual news headlines
    for headline in soup.find_all('a', class_='w_img'):  # Example class, adjust as needed
        text = headline.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

def scrape_toi_headlines_with_keyword(keyword):
    url = "https://timesofindia.indiatimes.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    # Adjusted selector to fetch actual news headlines
    for headline in soup.find_all('a', class_='w_img'):  # Example class, adjust as needed
        text = headline.get_text(strip=True)
        if text and keyword.lower() in text.lower():
            headlines.append(text)

    return headlines

# Example usage
if __name__ == "__main__":
    print("Fetching Times of India headlines containing the keyword 'bilateral'...")
    headlines = scrape_toi_headlines_with_keyword("bilateral")
    print("Filtered Headlines:", headlines)
