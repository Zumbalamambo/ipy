#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path


rootdir = u'E:/4 国家、行业标准'

# 指明被遍历的文件夹
# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

rp = {
    'JB T': 'JBT'
}

for parent, dirnames, filenames in os.walk(rootdir):
    for fn in filenames:
        filedir = os.path.join(parent, fn)

        for k, v in rp.items():
            if k in filedir:
                print(filedir)
                newfiledir = filedir.replace(k, v)
                print(newfiledir)
                try:
                    os.rename(filedir, newfiledir)
                except os.error as identifier:
                    print (identifier)

                

input('press enter...')
