#!/usr/bin/python3

from datetime import datetime

# dt1 = datetime.strptime('Jun 1 2018 5:33PM', '%b %d %Y %I:%M%p')
# print(dt1)

# dt2 = datetime.strptime('23:33:45', '%H:%M:%S')
# print(dt2.time())

ds = 'August 20 2020'
dt3 = datetime.strptime(ds, '%B %d %Y')
print(dt3)