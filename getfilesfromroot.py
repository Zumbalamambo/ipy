#!/usr/bin/env python2
# vim: set file encoding=gbk

import os
import os.path


rootdir = 'C:/Users/shenbo/Pictures/tiny/'

# ָ�����������ļ���
#�����������ֱ𷵻�1.��Ŀ¼ 2.�����ļ������֣�����·���� 3.�����ļ�����

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print rootdir, filename