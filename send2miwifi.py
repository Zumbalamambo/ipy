#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Usage: ./d2r.py RESOURCE_URL
'''

import base64, sys, requests

API = 'https://d.miwifi.com/d2r/download2Router'
headers = {'Cookie': 'xxxxxxxx'}
payload = dict()
#testurl = 'magnet:?xt=urn:btih:f400e5aebe7651e8be1d53d11de5f2f505742d43&dn=RoboCop.2014.1080p.BluRay.AVC.DTS-HD.MA.5.1-PublicHD&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337'
testurl = sys.argv[1]
payload['serviceToken'] ='xxxxxx'
payload['xiaoqiang_d2r_ph'] ='xxxxxx=='
payload['url'] = base64.b64encode(testurl)
payload['userId'] ='xxxxx'
payload['deviceId'] ='xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx'


r = requests.post(API, data=payload, headers=headers)
if r.text.encode('utf-8').find('成功添加下载') != -1: 
	print('DONE')
else:
	print('failed')