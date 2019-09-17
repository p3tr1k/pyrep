import datetime


now = datetime.date.today()

delta = now + datetime.timedelta(days=60)

print(delta.weekday())
