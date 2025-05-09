from news import scrape_toi_headlines
from cal import get_google_calendar_events
from weather import fetch_weather_data_
from sendmail import send_email

def aggregate_data():
    """
    Aggregates data from news, calendar, and weather modules into a dictionary of lists.

    Returns:
        dict: Aggregated data.
    """
    # Fetch news headlines
    news_headlines = scrape_toi_headlines()

    # Fetch calendar events
 #   try:
 #       calendar_events = get_google_calndar_events()
 #   except Exception as e:
 #       calendar_events = [f"Error fetching calendar events: {e}"]

    # Fetch weather data
    lat, lon = 33.44, -94.04  # Example coordinates
    api_key = "0a30c51aec587aa1289546d8bccc3cbd"  # Replace with your Weatherstack API key
    try:
        weather_data = fetch_weather_data_(lat, lon, api_key)
        weather_list = [
            {"temperature": weather_data['current']['temperature']},
            {"humidity": weather_data['current']['humidity']}
        ]
    except Exception as e:
        weather_list = [f"Error fetching weather data: {e}"]

    # Aggregate data into a dictionary
    aggregated_data = {
        "news": news_headlines,
        #"tasks": calendar_events,
        "weather": weather_list
    }

    return aggregated_data

if __name__ == "__main__":
    data = aggregate_data()
    print("Aggregated Data:", data)

    # Prepare email content
    subject = "Aggregated Data Report"
    body = f"Here is the aggregated data:\n{data}"

    # Send the email
    send_email(subject, body)