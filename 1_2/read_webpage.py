#!/usr/bin/env python3

import requests as req

resp = req.get("http://www.webcode.me")

print(resp.text)