#!/usr/bin/python3

import re
import requests

# content = '''<p>The <code>Pattern</code> is a compiled
# representation of a regular expression.</p>'''

resp = requests.get("http://webcode.me")
content = str(resp.content,'utf-8')

pattern = re.compile(r'[>.*<]+')

found = re.findall(pattern, content)

for tag in found:
    print(tag)