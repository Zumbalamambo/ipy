#!/usr/bin/env python2
# vim: set file encoding=gbk

import base64

'''
�ĵ���һ�����ص�С��·����
api��ַ: https://d.miwifi.com/d2r/?url=_Base64_&name=_name_&src=_src_

�����б�
url:    Base64��������ص�ַ��֧�ֵ��������ͣ�http��ftp��BT�������ӡ���¿ed2k��Ѹ��thunder��
ע��    ����ʹ�õ�Base64�㷨��ο�RCF 4648��ġ�Base 64 Encoding with URL and Filename Safe Alphabet�����ο�ʵ�֣�base64.js��
name:   ��Ҫ���ص��ļ�������ѡ����
src:    ��Դ���루��ѡ����

example
url: http://v.gorouter.info/20131204/С�׵�һ��.mp4
api: http://d.miwifi.com/d2r/?url=aHR0cDovL3YuZ29yb3V0ZXIuaW5mby8yMDEzMTIwNC_lsI_nsbPnmoTkuIDlpKkubXA0&src=demo

'''


def d2r(url):
    url2Base64 = "http://d.miwifi.com/d2r/?url=" + base64.encodestring(url)
    print url2Base64

url = 'http://v.gorouter.info/20131204/С�׵�һ��.mp4'
print url
d2r(url)

