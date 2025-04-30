import requests
from bs4 import BeautifulSoup

def get_cnn_top_news():
    url = "https://edition.cnn.com/world"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    # Find all headline elements (usually <h3> or <span> tags with specific classes)
    for headline in soup.find_all('span', class_='cd__headline-text'):
        headlines.append(headline.get_text(strip=True))

    return headlines

if __name__ == "__main__":
    print("Fetching top news from CNN World...")
    top_news = get_cnn_top_news()
    print("Top News Headlines:")
    for news in top_news:
        print(f"- {news}")