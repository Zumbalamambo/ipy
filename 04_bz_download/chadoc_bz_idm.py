#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import time
import requests
import re

'''
idm_dir       为IDM安装路径
IDM cmdline   idman /d URL [/p localdir] [/f filename] [/q] [/h] [/n] [/a]
/d URL        为下载链接
/p localdir   定义要保存的文件放在哪个本地路径
/f filename   定义要保存的文件到本地的文件名
/a            添加一个指定的文件到下载队列，但是不开始下载
'''


def dl_by_idm(dl_url, file_name):
    idm_dir = 'E:\SourceFiles\IDM\IDMan.exe'
    local_dir = 'D:'

    cmd = '{0} /a /d {1} /p {2} /f \"{3}\"'.format(
        idm_dir, dl_url, local_dir, file_name)
    print(cmd)

    # subprocess.Popen(cmd)
    time.sleep(0.2)


# 标准连接
bz_url = 'http://www.chadoc.com/v-{}.html'
# 标准下载链接
bz_dl_url = 'http://www.chadoc.com/?download={}&server=1'


def bz_dl():
    for i in range(1, 100):
        url = bz_url.format(str(i))
        # print(url)
        req = requests.get(url, ).content.decode(encoding='utf-8')
        # print(req)
        time.sleep(0.2)

        # <meta name="description" content="xxx.pdf" />
        reg = '<meta name="description" content="(.*?)" />'
        filename = re.search(reg, req, re.S).group(1)
        print(i, filename)
        if filename == '茶豆网':
            print(i, 'pass!')
            continue
        dl_url = bz_dl_url.format(str(i))
        print(dl_url)

        dl_by_idm(dl_url, filename)


if __name__ == '__main__':
    bz_dl()
