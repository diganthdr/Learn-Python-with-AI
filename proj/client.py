import requests

# API endpoint
url = "http://127.0.0.1:5000/api/v1/subscribe"

# Data to send to the API
data = {
    "name": "John",
    "emailid": "john.e@example.com"
}

# Make a POST request to the API
try:
    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 201:
        print("Success:", response.json())
    elif response.status_code == 409:
        print("Conflict:", response.json())
    elif response.status_code == 400:
        print("Bad Request:", response.json())
    else:
        print("Error:", response.status_code, response.json())
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)