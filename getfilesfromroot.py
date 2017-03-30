#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path


rootdir = 'C:/Users/shenbo/Pictures/tiny/'

# 指明被遍历的文件夹
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print rootdir, filename