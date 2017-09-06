#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests

'''
文档：一键下载到小米路由器
api地址: https://d.download2miwifi.com/d2r/?url=_Base64_&name=_name_&src=_src_

参数列表
url:    Base64编码的下载地址。支持的链接类型：http、ftp_server、BT磁力链接、电驴ed2k、迅雷thunder。
注：    这里使用的Base64算法请参考RCF 4648里的《Base 64 Encoding with URL and Filename Safe Alphabet》。参考实现：base64.js。
name:   需要下载的文件名（可选）。
src:    来源代码（可选）。

example
url: http://v.gorouter.info/20131204/小米的一天.mp4
api: http://d.download2miwifi.com/d2r/?url=aHR0cDovL3YuZ29yb3V0ZXIuaW5mby8yMDEzMTIwNC_lsI_nsbPnmoTkuIDlpKkubXA0&src=demo

'''

api = 'https://d.download2miwifi.com/d2r/'

url = 'http://v.gorouter.info/20131204/小米的一天.mp4'.encode(encoding='utf_8')
print(url)

post_data = {'url': base64.b64encode(url)}
print(post_data)

r = requests.post(api, data=post_data, verify=False)

print(r.text)

