#!/usr/bin/python3

import re

text = 'We met in 2013. She must be now about 27 years old. The film was called Ocean Eleven'

# pattern = re.compile(r'[A-Z][^\s.]+')

pattern = re.compile(r'[A-Z][a-z]\s+')

found = re.findall(pattern, text)

# if found:
    # print('There are {} numbers'.format(len(found)))
print(found)    

