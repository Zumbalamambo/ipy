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

# kk hosts
kk_hosts = '# kk hosts start\n' \
           '172.18.1.30 ekp.aerosun.cn\n' \
           '172.18.1.32 kk.aerosun.cn\n' \
           '# kk hosts end\n\n\n'
# ipv4 hosts url
ipv4_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
# windows hosts file dir
hosts_file_dir = 'C:/Windows/System32/drivers/etc/hosts'
desktop_dir = 'C:/Users/shenbo/Desktop/hosts'

print('loading hosts file...\n')

try:
    req = requests.get(ipv4_url)
    ipv4_hosts = req.content.decode(encoding='utf-8')
    print('got ipv4 hosts!\n')

except requests.HTTPError as e:
    print(e)
    raw_input()

t = time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time()))

hosts = kk_hosts + ipv4_hosts + '\n\n##hosts updated @ ' + t
print(hosts)

try:
    fd = os.open(hosts_file_dir, os.O_RDWR | os.O_CREAT)

    ret = os.write(fd, bytes(hosts, 'UTF-8'))
    print(ret)
    os.close(fd)

    input('hosts updated @ ' + t + ' !\npress enter!')

except IOError as e:
    print(e)

finally:
    fd = os.open(desktop_dir, os.O_RDWR | os.O_CREAT)

    ret = os.write(fd, bytes(hosts, 'UTF-8'))
    print(ret)
    fd.close()

    input('the host file has been saved on your desktop!')
