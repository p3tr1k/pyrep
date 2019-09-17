#!/usr/bin/env python3

import requests as req

resp = req.head("http://www.webcode.me")

print("Server: " + resp.headers['server'])
print("Last modified: " + resp.headers['last-modified'])
print("Content type: " + resp.headers['content-type'])