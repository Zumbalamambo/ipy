#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'shenbo'

import urllib
import urllib2
import re

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

url = 'http://172.18.64.3:8080/'
values = {'FunName': 'ncWebInternetLogin', 'username': '20953', 'password': '111111'}
values1 = {'FunName': 'ncWebInternetLogin','username': '20952', 'password': '111111'}
values2 = {'FunName': 'ncWebInternetLogin','username': '20635', 'password': '111111'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

# html = response.read()
# print html.decode("GB2312").encode('utf-8')
# page = response.read()