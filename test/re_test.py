#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import re

# dir = 'C:/Users/shenbo/Documents/GitHub/ipy/test.html'

# htmlfile = os.open(dir, os.O_RDWR)

# html = os.read(htmlfile, 5000).decode(encoding='utf-8')

# print (html)

# reg = '([0-9]*).html'

# g = re.findall(reg, html, re.S)
# print(g)


str = '<a href="http://www.down.bzko.com/201604/20160420QTBZ/NBT20010.12010.rar" style="color:#000000">点击下载该标准</a>'

reg = 'www.down.bzko.com(.*?).rar'

g = re.search(reg, str, re.S).group(1)
print(g)