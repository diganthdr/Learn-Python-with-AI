import requests
import requests
import json
def fetch_weather_data_(lat, lon, api_key="0a30c51aec587aa1289546d8bccc3cbd"):
    """
    Fetch weather data from Weatherstack API.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        api_key (str): API key for authentication.

    Returns:
        dict: Weather data as a JSON object, or None if the request fails.
    """
    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": f"{lat},{lon}"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        breakpoint()
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        if "error" in data:
            print(f"Error from Weatherstack API: {data['error']['info']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
        return None


def fetch_weather_data(lat, lon, exclude="hourly,daily", api_key="8ce4c729ceea8e65a62c843737ac8baf"):
    """
    Fetch weather data from OpenWeatherMap API.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        exclude (str): Data to exclude (e.g., "hourly,daily").
        api_key (str): API key for authentication.

    Returns:
        dict: Weather data as a JSON object, or None if the request fails.
    """
    url = f"https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": exclude,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
        return None

# Example usage
if False:
    lat = 33.44
    lon = -94.04
    weather_data = fetch_weather_data_(lat, lon)
    if weather_data:
        print("Weather Data:", weather_data)

# Example usage
if __name__ == "__main__":
    lat = 33.44
    lon = -94.04
    api_key = "0a30c51aec587aa1289546d8bccc3cbd"  # Replace with your Weatherstack API key
    weather_data = fetch_weather_data_(lat, lon, api_key)
    if weather_data:
        print("Weather Data:", weather_data)