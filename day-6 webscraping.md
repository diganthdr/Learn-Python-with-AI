
# 🌐 Web Scraping with Python

---

## 🧠 What is Web Scraping?

Web scraping is the process of automatically extracting data from websites. It's useful for collecting information like product prices, news, weather, etc.

---

## 🧰 Tools You'll Use

### 1. `requests`
To send HTTP requests and get the webpage content.

### 2. `BeautifulSoup`
To parse HTML and extract data from it.

---

## 📦 Installation

```bash
pip install requests
pip install beautifulsoup4
```

---

## 🧪 Basic Example

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Get the webpage
url = "https://example.com"
response = requests.get(url)
html = response.text

# Step 2: Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract Data
title = soup.title.text
print("Page Title:", title)
```

---

## 🔍 Useful Methods in BeautifulSoup

- `soup.find('tag')`: Finds the first occurrence of a tag.
- `soup.find_all('tag')`: Finds all occurrences.
- `element.text`: Gets the inner text.
- `element['href']`: Gets an attribute (like a link).

---

## ⚠️ Web Scraping Tips

- Always check the website's `robots.txt` to see what you're allowed to scrape.
- Don't overload a server with too many requests.
- Use `headers` to simulate a real browser.

**Example:**
```python
headers = {
    "User-Agent": "Mozilla/5.0"
}
requests.get(url, headers=headers)
```

---

## 🔐 Ethical Scraping

- Avoid scraping behind logins unless permitted.
- Use public APIs if available.
- Respect website terms of service.

---

Ready to scrape? 🚀
