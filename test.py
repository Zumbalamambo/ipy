#!/usr/bin/env python2
# vim: set file encoding=utf8


import subprocess
import time

# 用IDM下载歌单中的歌曲，download songs in playlist by idm
# ID            为歌单id
# idm_dir       为IDM安装路径
# IDM cmdline   idman /d URL [/p localdir] [/f filename] [/q] [/h] [/n] [/a]
# /d URL        为下载链接
# /p localdir   定义要保存的文件放在哪个本地路径
# /f filename   定义要保存的文件到本地的文件名
# /a            添加一个指定的文件到下载队列，但是不开始下载

idm_dir = u'C:\Program Files\Internet Download Manager\idman.exe'
biaozhunurl = u'http://www.chadoc.com/?download=%d&server=1'
for i in range(1000,1010):
    url = 'http://www.chadoc.com/?download=%d&server=1' % i
    print url
    cmd = '%s /a /d \"%s\" /f \"%s.pdf\"' % (idm_dir, url, i)
    print cmd
    cmd = cmd.encode('gbk')
    subprocess.Popen(cmd)
    time.sleep(0.5)
