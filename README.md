# tennis_booking

<pre>

Procedure:

1. Turn on Google Calender API using the process mentioned in the following link 
   https://developers.google.com/google-apps/calendar/quickstart/python#prerequisites
2. Used Google Event Insert API call for inserting an event i.e every Saturday 6:00 - 7:300 tennis court should be reserved 
   API : POST https://www.googleapis.com/calendar/v3/calendars/calendarId/events
3. Written necessary event reservartion logic in Booking.py file
4. Script file job.sh has been written for executing Booking.py code for reservation event.
5. Path name for script file and log file is given for cronjob 

Cronjob: 
0 0 * * 0 /Users/Raja/IDE/Eclipse-Python/workspace/TennisBooking/job.sh >> /Users/Raja/IDE/Eclipse-Python/workspace/TennisBooking/test.log 2>&1

Every sunday, the cron job will be run to reserve the tennis court 

6. The successful booking details will be logged in to Test.log file in the same folder of source code.


</pre>
