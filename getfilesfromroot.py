#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path


rootdir = u'E:/2 Projects/201610 中核干燥器/03 项目文件/03 方案评审准备材料/桶内干燥装置 方案评审资料/'

# 指明被遍历的文件夹
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

for parent, dirnames, filenames in os.walk(rootdir):
    for fn in filenames:
        print fn

raw_input()