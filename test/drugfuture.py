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


def binarizing(img, threshold=128):
    """
    图片二值化处理.

    :param img:         PIL Image.
    :param threshold:   (default 128).
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


def dl_CN_Patent(patent_no):
    """
    中国专利下载.

    :param patent_no:  专利申请号（CN2016xxxxxxxx.x）
    """

    # 地址 url
    df_url = 'http://www.drugfuture.com/cnpat/cn_patent.asp'
    captcha_url = 'http://www2.drugfuture.com/cnpat/verify.aspx'
    captcha_pic_url = 'http://www2.drugfuture.com/cnpat/VerifyCode.aspx'
    resault_url = 'http://www2.drugfuture.com/cnpat/search.aspx'

    # data
    form_data = {'cnpatentno': patent_no,
                 'Common': '1'
                 }

    mysession = requests.Session()
    cap = mysession.get(captcha_pic_url, data=form_data, timeout=60 * 4)

    imgBuf = BytesIO(cap.content)
    image = Image.open(imgBuf)
    image.show()

    # image = image.convert('L')
    # image.show()
    # image = binarizing(image)
    # image.show()
    # vcode = pytesseract.image_to_string(image, lang='eng')
    # print(vcode)

    validcode = input('iii')

    form_data = {'cnpatentno': patent_no,
                 'Common': '1',
                 'ValidCode': validcode
                 }
    result = mysession.post(resault_url, data=form_data, timeout=60 * 4)
    print(result.content.decode("utf-8"))


valipatent_no = input('uuu')

dl_CN_Patent(valipatent_no)
