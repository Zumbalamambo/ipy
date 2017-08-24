import time
from wxpy import *

import gold_price


if __name__ == '__main__':

    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True)
    xinxin = bot.friends().search('欣欣')[0]

    while True:
        p = gold_price.get_gold_price()
        # print(p)

        msg = '实时价格:{0}元/克\n上浮/下降:{1}元/克({2})\n'
        msg = msg.format(p[0], p[1], p[2])

        # 发送消息给自己和欣欣
        bot.self.send(msg)
        # xinxin.send(msg)
        time.sleep(3600)
    # embed()