import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_summary():
    url = "https://en.wikipedia.org/wiki/Prompt_engineering"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    summary = ""

    for paragraph in paragraphs[:3]:  # Extracting the first three paragraphs as a summary
        summary += paragraph.get_text(strip=True) + "\n"

    return summary

if __name__ == "__main__":
    print("Fetching summary of the Wikipedia page on Prompt Engineering...")
    summary = scrape_wikipedia_summary()
    print("Summary:", summary)