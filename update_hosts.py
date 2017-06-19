#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
notepad c:/windows/system32/drivers/etc/hosts

shenbo@hotmail.com
@ 2013.01.20
"""

import os
import sys
import requests
import time

kk_hosts = '# kk hosts start\n' \
           '172.18.1.30 ekp.aerosun.cn\n' \
           '172.18.1.32 kk.aerosun.cn\n' \
           '# kk hosts end\n\n'

ipv4_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'

hosts_file_dir = 'C:/Windows/System32/drivers/etc/hosts'
desktop_dir = 'C:/Users/shenbo/Desktop/hosts'


def gethosts():
    print('loading hosts file...\n')
    try:
        req = requests.get(ipv4_url)
        ipv4_hosts = req.content.decode(encoding='utf-8')
        print('got ipv4 hosts!\n')
    except requests.HTTPError as e:
        print(e)
        input()

    now = time.localtime(time.time())
    tm = time.strftime('%Y-%m-%d, %H:%M:%S', now)
    s = '\n\n##hosts updated @ ' + tm

    hosts = kk_hosts + ipv4_hosts + s
    return hosts


def updatehosts(hosts):
    with open(hosts_file_dir, 'wb') as fd:
        fd.write(bytes(hosts, 'UTF-8'))

    with open(desktop_dir, 'wb') as fd:
        fd.write(bytes(hosts, 'UTF-8'))

    input('hosts updated succeed !\npress enter!')


if __name__ == '__main__':
    h = gethosts()
    updatehosts(h)
