from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from datetime import datetime,tzinfo,timedelta
import datetime
import time

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'clientx.json'
APPLICATION_NAME = 'Tennis'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('./')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir,mode=0777)

    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart2.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
    return credentials

def main():

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    arr=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    index=arr.index(time.strftime("%A"))

    book_index=6-index;
    if book_index==0:
        book_index=7

    book_date=datetime.datetime.now() + datetime.timedelta(days=book_index)
    newdate_start = book_date.replace(hour=06, minute=00, second=00, microsecond=00)
    newdate_end = book_date.replace(hour=07, minute=30, second=00, microsecond=00)
    newdate_start=newdate_start.strftime("%Y-%m-%dT%H:%M:%S-04:00")
    newdate_end=newdate_end.strftime("%Y-%m-%dT%H:%M:%S-04:00")


    booking_thisweek=datetime.datetime.now() + datetime.timedelta(days=7)


    # eventsResult = service.events().list(
    #     calendarId='primary', timeMin=now,maxResults=10, singleEvents=True,orderBy='startTime').execute()
    #
    # events = eventsResult.get('items', [])
    #
    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     if event['summary']:
    #         print(start, event['summary'])



    event = {'summary': 'Tennis Court Reservation- Reserved by Venkata Ganti','location': 'Cinco Ranch, 25202 Springwood Lake Dr.,Katy,TX-77494',
             'description': 'Venkata Ganti has reserved tennis court',
             'start': {
                 'dateTime': newdate_start,
                 'timeZone': 'America/Swift_Current',
             },
             'end': {
                 'dateTime': newdate_end,
                 'timeZone': 'America/Swift_Current',
             },
             # 'recurrence': ['RRULE:FREQ=DAILY;COUNT=1'],
             'attendees': [{'email': 'venkata.ganti@gmail.com'},],
             'reminders': {'useDefault': False,'overrides': [{'method': 'email', 'minutes': 24 * 60},
                                                             {'method': 'popup', 'minutes': 10},
                                                             ],
                           },
             }

    e = service.events().insert(calendarId='primary', body=event).execute()

    print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))

    print('Event created: %s' % (e.get('htmlLink')))

if __name__ == '__main__':
    main()