### Date ### 

from datetime import datetime as Date, time
date = Date.now()

print(date.day)
print(date.year)
print(date.second)
print(date.minute)
print(date.month)


## timestamp ##

time__now = date.timestamp()
print(time__now)

year_2023 = date.isoweekday()
print(year_2023)

datetime = time(date.hour, date.minute, date.second)
print(datetime)

now = date.today()
print(now)