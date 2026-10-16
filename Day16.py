# Day 16 - Datetime
# The datetime library is a built-in python library that contains almost all functionality related to dates and time,
# from constructing time strings to switching timezones to even getting the current timestamp.
from datetime import datetime, time, date, timedelta

print(datetime.now()) # 2026-10-16 15:18:25.510924
formatted_time = datetime.strftime(datetime.now(),"%m/%d/%Y, %H:%M:%S")
print(formatted_time)

ex3 = date(2019,12,5)
print(ex3)

today = date.today()
newYear = date(2026,12,30)
diff = newYear - today
print(diff) # 75 days

oldDate = date(1970,1,1)
diff2 = today - oldDate
print(diff2) # 20742 days

# This library seems very usefull for any app that uses python, the course brings up a few examples and i can bring up some too
# like a pomodoro timer app that helps you focus, or a calendar management app that links to google so you can check from the terminal.
# definetly gonna make a project using this library, when i do i'll link the github here:

# Day 16 - Done!