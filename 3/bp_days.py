import datetime


dob = datetime.date(1963, 12, 18) #ymd
now = datetime.date.today()

delta = now - dob

print(delta.days)