from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import requests


def get_google_calendar():
    """
    This function gets the data from a specific google calander. In this case the program is
    looking at the calender of the gmail workvalvesem@gmail.com. If it gives errors with the
    credentials, delete the token.json, rerun the program and log into the website using the
    password h1IUB$3WQK.
    :param task_list: a list of the current tasks
    :return: the list with the current tasks and the tasks added from the google calendar.
    """
    # If modifying these scopes, delete the file token.json.
    scopes = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('APIs/token.json'):
        creds = Credentials.from_authorized_user_file('APIs/token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('APIs/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('APIs/token.json', 'w', encoding='utf-8') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API and get the info you need
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    end_time = datetime.date.today().isoformat() + 'T23:59:59.00Z'
    print('Getting the tasks of today')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          timeMax=end_time, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    start_time = []
    end_time = []
    description = []
    if not events:
        print('No meetings in google calender for today')
    for event in events:
        # Put starttime, endtime and name in list
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))

        start_time = start_time.append(int(start[11:13] + start[14:16]))
        end_time = end_time.append(int(end[11:13] + end[14:16]))
        description = description.append(event['summary'])
        print("Added " + event['summary'] + " to your WorkValve calendar")

    return start_time, end_time, description


def get_weather(city):
    # set the api key and the url of the weather website
    api_key = "094eaa9002d7545fbda3e4c9f5956fe9"
    base_url = "https://api.openweathermap.org/data/2.5/forecast?"
    # complete url
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    # get the info from the API
    response = requests.get(complete_url)
    data = response.json()
    # check if the city exists
    if data["cod"] != "404":
        return data
    else:
        print("City not found")
        return None
