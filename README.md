# Zoom Korona - Never forget to join another Zoom meeting
Script to join zoom calls automatically by pulling scheduling data from Google Sheets and Google calendar

Instructions for Google Calendar Integration
* Go to https://developers.google.com/calendar/quickstart/python and Enable Google Calendar API. Also download Client configuration file (credentials.json) and move it to /CalendarAPI folder.
* Run ```pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```
* Run ```$python zoomCalendar.py``` and complete google calender quick start login authentication in the browser.
* Add your event to google calender with time and paste the url in description of the event.
* Hola! run ```$python zoomCalendar.py``` again and enjoy!

Instructions for Google Sheets Integration
* Watch demo: https://youtu.be/qwrn6SzWkjk

