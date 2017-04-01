#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import sys
import requests

# url
testurl = b'https://static.oschina.net/uploads/user/27/54100_100.jpg?t=1369018818000'

# api地址
API = 'https://d.miwifi.com/d2r/download2RouterApi'

# cookie
cookie = 'lastUsedDeviceId=0c9a7f7e-7577-8d75-827d-cd2173ecba64; JSESSIONID=aaaUfhIXNqBIO77IaLWRv; serviceToken=1LZJ3kbjnNNAhQ2q9qPWUMcKehocd8xhLW+7+VyDxndHoxniTj5FZpH8RyEflWs2xO0fVXgzeYJEPBwspW7gwj8lwvbfX63yslKfg0DWDpK4EaLXwNxjuRiLGBrANJ/hRnspA/7irX9lJ/9mqpobug==; userId=42544989; xiaoqiang_d2r_slh=19mBBhFE0ZvCxYrwo1ld5XWNBts=; xiaoqiang_d2r_ph=2fmWayCj3M3DqCiVCzHhTw==; Hm_lvt_8a095beeafdd3f76ea11be6de7eed2a4=1490263103,1490864485,1490864650,1490865316; Hm_lpvt_8a095beeafdd3f76ea11be6de7eed2a4=1490865396; lastUsedDeviceId=0c9a7f7e-7577-8d75-827d-cd2173ecba64'

headers = {'Cookie': cookie}
print(headers)

# data
url = base64.b64encode(testurl)
userId = '42544989'
deviceId = '0c9a7f7e-7577-8d75-827d-cd2173ecba64'
serviceToken = '1LZJ3kbjnNNAhQ2q9qPWUMcKehocd8xhLW+7+VyDxndHoxniTj5FZpH8RyEflWs2xO0fVXgzeYJEPBwspW7gwj8lwvbfX63yslKfg0DWDpK4EaLXwNxjuRiLGBrANJ/hRnspA/7irX9lJ/9mqpobug=='
xiaoqiang_d2r_ph = '2fmWayCj3M3DqCiVCzHhTw=='

post_data = {'url': url,
             'userId': userId,
             'deviceId': deviceId,
             'serviceToken': serviceToken,
             'xiaoqiang_d2r_ph': xiaoqiang_d2r_ph
             }
print(post_data)

# requests
r = requests.post(API, data=post_data, headers=headers, verify=False)

print(r.text)
