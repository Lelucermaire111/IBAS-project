#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
import json
import base64

with open('Office.jpg', 'rb') as f:
    data = f.read()
payload = {'token': 'vri2WxoOYizhWcvJ', 'taskid': 'im2txt0914','data':base64.b64encode(data)}
r = requests.post("http://api.noperfect.cn/api/task", data=payload)
print(r.text)
print(json.dumps(r.text))