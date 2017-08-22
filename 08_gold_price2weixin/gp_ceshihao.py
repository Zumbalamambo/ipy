import requests
import json

import gold_price

App_id = 'wxad3edefbef3f17ed'
App_secret = 'c2653ec7375e8c18ca5852c3e51901bf'

Open_id = 'optBY1qs60rcq2ds-hQXg2QoCheg' #xixishuiba
Open_id2 = 'optBY1qibJd5BE8936qSgL6gAKvY' #xinxin

Template_id = '6uCOppBXxH94e2PBWVNl6xuTw9tSJYyHTaH7uUm18h4'


def get_access_token():
    token_url = 'https://api.weixin.qq.com/cgi-bin/token?'
    post_data = {'grant_type': 'client_credential',
                 'appid': App_id,
                 'secret': App_secret}

    req = requests.post(token_url, data=post_data)
    j = req.content.decode(encoding='utf-8')
    result = json.loads(j)

    access_token = result['access_token']
    expires_in = result['expires_in']
    print('access_token:', access_token)
    print('expires_in:', expires_in)

    return access_token


def get_users(token):
    user_url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='
    user_url += token

    req = requests.get(user_url)
    j = req.content.decode(encoding='utf-8')
    print(j)


def send_text_msg(token, user_id, msg):
    send_url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token='
    send_url += token

    d = dict(touser=user_id, msgtype='text', text=dict(content=msg))
    body = json.dumps(d, indent=4)
    print(body)

    req2 = requests.post(send_url, json=body)
    # jj = req2.content.decode(encoding='utf-8')
    # print(jj)


def send_template_msg(token, user_id, price, swing, swingrange):
    send_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='
    send_url += token

    data = {'price': {'value': price, 'color': '#173177'},
            'swing': {'value': swing, 'color': '#173177'},
            'swingrange': {'value': swingrange, 'color': '#173177'}}

    d = {'touser': user_id,
         'template_id': Template_id,
         'url': 'http://www.dyhjw.com/hjtd/',
         'topcolor':'#FF0000',
         'data':data}
    body = json.dumps(d, indent=4)
    # print(body)

    req2 = requests.post(send_url, body)
    # jj = req2.content.decode(encoding='utf-8')
    # print(jj)


if __name__ == '__main__':
    p = gold_price.get_gold_price()
    print(p)

    token = get_access_token()
    # access_token = '_laZISLWl8fdCphcMzp66rUGas2KVu8NiqeztRYviLMR1L0FRRrLKel3WFmzJIYSlTJaZsActOgOd9G6zv21mc59GgES884viUFKUPxx_de1rJH0nNTrNllm0GYVTdQdTFTgABAZLZ'

    # get_users(access_token)
    # send_text_msg(access_token, Open_id, 'hello')
    
    send_template_msg(token, Open_id, p[0], p[1], p[2])
    # send_template_msg(token, Open_id2, p[0], p[1], p[2])
    




