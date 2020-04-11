from __future__ import print_function
import datetime
import pickle
import time
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import webbrowser

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_event(creds, service):

    #DOESN'T WORK WITHOUT THIS
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    nowist = datetime.datetime.now()

    #GETTING THE UPCOMING EVENT
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        exit()
        
    start = events[0]['start'].get('dateTime', events[0]['start'].get('date'))
    time = start[:16]

    #print(time)

    #FOR FULL DAY EVENTS
    if(start[17:]==""):
        print("Next event is a full day event")
        return 0
    
    record_time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M')

    if(nowist.month<record_time.month):
        print("Next event is not this month")
        return 0

    if(nowist.day<record_time.day):
        print("Next event is not today")
        return 0

    print("Found Event happening today!")


    rec_timeVal = int(str(record_time.hour)+str(record_time.minute))
    now_timeVal = int(str(nowist.hour)+str(nowist.minute))

    #print("rec_timeVal: ", rec_timeVal)
    print("Current Time:", now_timeVal)

    if(now_timeVal>rec_timeVal-5 and now_timeVal<rec_timeVal+5):
        print("Event time matches current time! LAUNCHING...")
        #zoom_url = events[0]['description']
        #webbrowser.open_new_tab(zoom_url)
        return 1
        #flag = 1
        #break   
    
    print("NEXT EVENT: ", record_time, events[0]['summary'])

    return 0
    

    


def main():

    try:
    
        #AUTHENTICATION START--------------------------------------------------------------------------------
        
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
                
        #AUTHENTICATION END------------------------------------------------------------------------------

        service = build('calendar', 'v3', credentials=creds)

        while(get_event(creds, service)!=1):
            #HOW LONG TO SLEEP FOR IN SECONDS
            time.sleep(10)

    except:
        print("Please check your internet connection")
        time.sleep(10)
        main()    

if __name__ == '__main__':
    main()
