#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import time


# get gold price
def gold_price():

    gold_url = 'http://www.dyhjw.com/hjtd/'

    req = requests.get(gold_url, ).content.decode(encoding='utf-8')
    # print(req)
    '''
    <span class="nom last">{%}</span>
    <font class="swing">{%}</font>
    <font class="swingRange">{%}</font>
    
    <li>今开：<font>{%}</font></li>
    <li>最高：<font>{%}</font></li>
    <li >总量：<font>{%}</font></li>
    <li>昨收：<font>{%}</font></li>
    <li>最低：<font>{%}</font></li>
    <li >昨结：<font>{%}</font></li>
    '''
    key = []

    reg = ['<span class="nom last">(.*?)</span>',
           '<font class="swing">(.*?)</font>',
           '<font class="swingRange">(.*?)</font>']
    for i in reg:
        key.append(re.search(i, req, re.S).group(1))

    gold_td_now = '实时价格:{0}元/克 \n\n上浮/下降:{1}元/克({2})\n'
    gold_td_now = gold_td_now.format(key[0], key[1], key[2])

    # reg1 = '<font>(.*?)</font></li>'
    # k = (re.findall(reg1, req, re.S))
    # gold_td_today = '今开:{0}, 最高:{1}，总量:{2}\n' + '昨收:{3}, 最低:{4}，昨结:{5}'
    # gold_td_today = gold_td_today.format(k[0], k[1], k[2], k[3], k[4], k[5])

    return gold_td_now


def send_to_ftqq(t, d):
    sckey = 'SCU10033T5f9a872874ef8f9babb7f5db7f198c855964a3909aa42'
    api = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(sckey, t, d)

    requests.post(api)


if __name__ == '__main__':
    gp = gold_price()
    # print(gp)
    # now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    send_to_ftqq('Gold Price', gp)