#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import time
import requests
import re
import os

'''
用IDM下载歌单中的歌曲，download songs in playlist by idm
ID            为歌单id
idm_dir       为IDM安装路径
IDM cmdline   idman /d URL [/p localdir] [/f filename] [/q] [/h] [/n] [/a]
/d URL        为下载链接
/p localdir   定义要保存的文件放在哪个本地路径
/f filename   定义要保存的文件到本地的文件名
/a            添加一个指定的文件到下载队列，但是不开始下载
'''

# IDM安装路径
html_dir = 'C:/Users/shenbo/Documents/GitHub/ipy/test.html'

# 标准链接
bz_url = 'http://www.bzko.com/Common/ShowDownloadUrl.aspx?urlid=0&id={}'


# 标准链接
bz_dl_url = 'http://www.down.bzko.com{}.rar'



# 下载到本地的保存路径
download2localdir = 'D:'

dir = 'C:/Users/shenbo/Documents/GitHub/ipy/test.html'

htmlfile = os.open(dir, os.O_RDWR)

html = os.read(htmlfile, 5000).decode(encoding='utf-8')

print (html)

reg = '([0-9]*).html'

g = re.findall(reg, html, re.S)
print(g)



for i in g:
    url = bz_url.format(i)
    # print(url)
    req = requests.get(url,).content.decode(encoding='utf-8')

    time.sleep(0.5)
    # <a href="http://www.down.bzko.com/201604/20160420QTBZ/NBT20010.12010.rar" style="color:#000000">点击下载该标准</a>
    reg = 'www.down.bzko.com(.*?).rar'

    g = re.search(reg, req, re.S).group(1)
    print(bz_dl_url.format(g))