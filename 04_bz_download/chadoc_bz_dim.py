#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import time
import requests
import re

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
idm_dir = 'E:\SourceFiles\IDM\IDMan.exe'

# 标准连接
bz_url = 'http://www.chadoc.com/v-{}.html'

# 标准下载链接
bz_dl_url = 'http://www.chadoc.com/?download={}&server=1'

# 下载到本地的保存路径
download2localdir = 'D:'


def bz_dl():
    for i in range(1, 1700):
        print('NO:' + str(i))

        url = bz_url.format(str(i))
        # print(url)
        req = requests.get(url, ).content.decode(encoding='utf-8')
        # print(req)
        time.sleep(0.5)
        # <meta name="description" content="xxx.pdf" />
        reg = '<meta name="description" content="(.*?)" />'
        filename = re.search(reg, req, re.S).group(1)
        print(filename)
        if filename == '茶豆网':
            print('pass!')
            continue
        dl_url = bz_dl_url.format(str(i))
        print(dl_url)

        # cmd = '\"{}\" /a /d \"{}\" /f {}.pdf'.format(idm_dir, url, str(i))

        cmd = '{0} /a /d {1} /p {2} /f \"{3}\"'.format(
            idm_dir, dl_url, download2localdir, filename)
        print(cmd)

        # subprocess.Popen(cmd)
        time.sleep(0.5)


if __name__ == '__main__':
    bz_dl()
