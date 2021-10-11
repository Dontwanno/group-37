from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from classes import Task
# from classes import TaskList

# For the testing purposes of this project there is a testing gmail workspace
# Mail: workvalvesem@gmail.com
# Password: h1IUB$3WQK
# This mail has already been configured.
# DONT CHANGE OR DELETE THE credentials.json and token.json files


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_google_calendar(task_list):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('api_folder/token.json'):
        creds = Credentials.from_authorized_user_file('api_folder/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('api_folder/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # I don't know if utf-8 is correct, else change it to ascii
        with open('api_folder/token.json', 'w', encoding='utf-8') as token:
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
    if not events:
        print('No tasks planned for today')
    for event in events:
        # Put starttime, endtime and name in list
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))

        start_time = int(start[11:13] + start[14:16])
        end_time = int(end[11:13] + end[14:16])
        description = event['summary']
        task_list.add_task(Task(start_time, end_time, description, True))

        print("Added " + event['summary'] + " to your WorkValve calendar")

    return task_list
