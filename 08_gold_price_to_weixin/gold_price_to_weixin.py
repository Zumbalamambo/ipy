#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import time
from wxpy import *


# get gold price
def gold_price():

    gold_url = 'http://www.dyhjw.com/hjtd/'

    req = requests.get(gold_url, ).content.decode(encoding='utf-8')
    # print(req)

    # <span class="nom last">{%}</span>
    # <font class="swing">{%}</font>
    # <font class="swingRange">{%}</font>
    # <li>今开：<font>{%}</font></li>
    # <li>最高：<font>{%}</font></li>
    # <li >总量：<font>{%}</font></li>
    # <li>昨收：<font>{%}</font></li>
    # <li>最低：<font>{%}</font></li>
    # <li >昨结：<font>{%}</font></li>

    key = []

    reg = ['<span class="nom last">(.*?)</span>',
           '<font class="swing">(.*?)</font>',
           '<font class="swingRange">(.*?)</font>']
    for i in reg:
        key.append(re.search(i, req, re.S).group(1))
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    gold_td_now = now + '\n实时价格:{0}元/克\n上浮/下降:{1}元/克({2})\n'
    gold_td_now = gold_td_now.format(key[0], key[1], key[2])

    # reg1 = '<font>(.*?)</font></li>'
    # k = (re.findall(reg1, req, re.S))
    # gold_td_today = '今开:{0}, 最高:{1}，总量:{2}\n' + '昨收:{3}, 最低:{4}，昨结:{5}'
    # gold_td_today = gold_td_today.format(k[0], k[1], k[2], k[3], k[4], k[5])

    return gold_td_now


if __name__ == '__main__':


    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True)
    xinxin = bot.friends().search('欣欣')[0]

    while True:
        gp = gold_price()
        # print(gp)
        # 发送消息给自己和欣欣
        bot.self.send(gp)
        # xinxin.send(gp)
        time.sleep(3600)
    # embed()