
# 🧠 Google Calendar API with OAuth2.0 - Class Notes & Assignment

## ✅ What We Learned
- How to authenticate with Google using OAuth2.0
- How to get access tokens securely
- How to call Google Calendar API to read today’s events

## 🛠 Tools Used
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## 🔐 OAuth2.0 Flow Recap
1. User grants permission through a browser.
2. OAuth2 flow completes using credentials and gets tokens.
3. Tokens are used to access Google Calendar API endpoints securely.

## 🧪 Example Code to Read Today’s Events
```python
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)

service = build('calendar', 'v3', credentials=creds)

now = datetime.utcnow().isoformat() + 'Z'
end_of_day = (datetime.utcnow() + timedelta(hours=23)).isoformat() + 'Z'

events_result = service.events().list(calendarId='primary', timeMin=now,
                                      timeMax=end_of_day, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
```

---

# 📚 Assignment

## 🎯 Objective
Explore more functionality of Google Calendar API and modify the sample.

### 📌 Part A: Show Next 10 Events
- Modify the sample code to display the next 10 upcoming events.
- Include both today and future events.
- Print the event name and start time.

### 📌 Part B: Add a New Event
- Update the code to create a new event in Google Calendar.
- Use static values like:
  - Summary: "VibeCoding Practice"
  - Start Time: 1 hour from now
  - End Time: 2 hours from now

📘 [Reference Docs](https://developers.google.com/calendar/api/v3/reference/events/insert)

## ✅ Hints
- Use `.events().insert(...)` method for creating events
- Use `datetime.now()` and `timedelta()` to calculate start & end times
- Set `"timeZone": "Asia/Kolkata"` for Indian time

## 🧠 Bonus Challenge
- Ask user to enter event title and time
- Create an event dynamically using their input
