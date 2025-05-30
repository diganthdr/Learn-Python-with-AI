from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_google_calendar_events():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8081)  # Starts the local server
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    print('Upcoming events:')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start} - {event['summary']}")

if __name__ == "__main__":
    get_google_calendar_events()