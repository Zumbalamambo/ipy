#!/usr/bin/env python2
# vim: set file encoding=gbk

import time
import wget

# 用WGET下载链接
# WGET  wget.download(url, filename or directory)

url = 'https://github.com/ShareX/ShareX/releases/download/v11.4.1/ShareX-portable.zip'
filename = 'ShareX-portable.zip'
wget.download(url, filename)
time.sleep(0.5)