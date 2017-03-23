#!/usr/bin/env python2
# vim: set file encoding=utf8

"""
notepad c:/windows/system32/drivers/etc/hosts

shenbo@hotmail.com
@ 2013.01.20
"""

import os, sys, urllib2, time

# kk hosts
kk_hosts = '# kk hosts start\n' \
           '172.18.1.30 ekp.aerosun.cn\n' \
           '172.18.1.32 kk.aerosun.cn\n' \
           '# kk hosts end\n\n\n'
# ipv4 hosts url
ipv4_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
# windows hosts file dir
hosts_file_dir = 'C:/Windows/System32/drivers/etc/hosts'

print u'loading hosts file...\n'

try:
    response = urllib2.urlopen(ipv4_url)
    ipv4_hosts = response.read()
    print u'got ipv4 hosts!\n'

except urllib2.HTTPError as e:
    print e
    raw_input()

t = time.strftime('%Y-%m-%d, %H:%M:%S',time.localtime(time.time()))

hosts = kk_hosts + ipv4_hosts + '\n\n##hosts updated @ ' + t

try:
    f = file(hosts_file_dir, 'w')
    f.write(hosts)
    f.close()
    raw_input('hosts updated @ ' + t + ' !\npress enter!')
except IOError as e:
    print e
finally:
    f = file('C:\Users\shenbo\Desktop\hosts', 'w')
    f.write(hosts)
    print 'find the host file on your desktop!'
    f.close()
    raw_input()

