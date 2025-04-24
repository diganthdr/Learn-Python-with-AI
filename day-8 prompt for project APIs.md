
# 🌐 Introduction to APIs in Python

---

## 🧠 What is an API?

API stands for **Application Programming Interface**. It allows two applications to talk to each other and exchange data.

---

## 🛠️ Using APIs with Python

To interact with an API, you usually:
1. Make an HTTP request (GET, POST, etc.)
2. Receive a response (usually in JSON format)
3. Parse and use the data in your code

---

## 📦 Required Library

```bash
pip install requests
```

---

## 🌤️ Weather API Example

We'll use the **OpenWeatherMap API** to get current weather data.

👉 Sign up at https://openweathermap.org/api and get your API key (free tier available).

---

## 🧪 Example Code

```python
import requests

API_KEY = "your_api_key_here"  # Replace with your actual API key
city = "Bangalore"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {city}:")
    print("Temperature:", data["main"]["temp"], "°C")
    print("Description:", data["weather"][0]["description"])
else:
    print("Error fetching data:", data.get("message", "Unknown error"))
```

---

## 🧪 Assignment

### ✅ Assignment 1: Get Weather for Any City
1. Ask the user for a city name using `input()`.
2. Call the API and show temperature and weather description.

### ✅ Assignment 2: Bonus - Add Error Handling
1. If the user types a wrong city name, handle it gracefully.
2. Print "City not found!" or show API error message.

---

## 💡 Pro Tips

- Always store your API keys securely (e.g., in environment variables).
- Read the API documentation to understand endpoints and parameters.

---

Happy Exploring APIs! 🚀
