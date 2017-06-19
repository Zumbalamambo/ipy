#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
中国专利全文下载 drugfuture : 
http://www.drugfuture.com/cnpat/cn_patent.asp

shenbo@hotmail.com
@ 2017.04.24
"""

import re
import subprocess
import time

import pytesseract
import requests
from PIL import Image
from io import BytesIO


def binarizing(img, threshold=192):
    """
    图片二值化处理.

    :param img:         PIL Image.
    :param threshold:   (default 64).
    :returns:           PIL Image.
    """
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


def cap_to_str(captcha_url):
    """
    验证码识别.
    """
    mysession = requests.Session()
    cap = mysession.get(captcha_url, timeout=60 * 4)

    imgBuf = BytesIO(cap.content)
    image = Image.open(imgBuf)
    # image.show()

    image = image.convert('L')
    # image.show()

    image = binarizing(image)
    # image.show()

    vcode = pytesseract.image_to_string(image, lang='eng')
    
    return vcode


cap_url = 'http://www2.drugfuture.com/cnpat/VerifyCode.aspx'

print (cap_to_str(cap_url))
