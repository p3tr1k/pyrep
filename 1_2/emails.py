#!/usr/bin/python3

import re

emails = ("luke@gmail.com", "andy@yahoocom", 
    "34234sdfa#2345", "f344@gmail.com")

pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')

for email in emails:
    if re.match(pattern, email):
        print("{} matches".format(email))
    else:
        print("{} does not match".format(email))