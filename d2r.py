#!/usr/bin/env python2
# vim: set file encoding=gbk

import base64

'''
文档：一键下载到小米路由器
api地址: https://d.miwifi.com/d2r/?url=_Base64_&name=_name_&src=_src_

参数列表
url:    Base64编码的下载地址。支持的链接类型：http、ftp、BT磁力链接、电驴ed2k、迅雷thunder。
注：    这里使用的Base64算法请参考RCF 4648里的《Base 64 Encoding with URL and Filename Safe Alphabet》。参考实现：base64.js。
name:   需要下载的文件名（可选）。
src:    来源代码（可选）。

example
url: http://v.gorouter.info/20131204/小米的一天.mp4
api: http://d.miwifi.com/d2r/?url=aHR0cDovL3YuZ29yb3V0ZXIuaW5mby8yMDEzMTIwNC_lsI_nsbPnmoTkuIDlpKkubXA0&src=demo

'''


def d2r(url):
    url2Base64 = "http://d.miwifi.com/d2r/?url=" + base64.encodestring(url)
    print url2Base64

url = 'http://v.gorouter.info/20131204/小米的一天.mp4'
print url
d2r(url)

