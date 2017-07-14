import requests
import urllib.request
import json
import re


App_id = 'wxad3edefbef3f17ed'

App_secret = 'c2653ec7375e8c18ca5852c3e51901bf'

Open_id = 'optBY1qs60rcq2ds-hQXg2QoCheg' #xixishuiba
Open_id2 = 'optBY1qibJd5BE8936qSgL6gAKvY' #xinxin


Template_id = '6uCOppBXxH94e2PBWVNl6xuTw9tSJYyHTaH7uUm18h4'


def get_access_token(id, secret):

    token_url = 'https://api.weixin.qq.com/cgi-bin/token?'

    post_data = dict(grant_type='client_credential', appid=id, secret=secret)

    req = requests.post(token_url, data=post_data)

    j = req.content.decode(encoding='utf-8')

    result = json.loads(j)
    access_token = result['access_token']
    expires_in = result['expires_in']
    print(access_token)
    return access_token


def send_text_msg(token, userid, msg):
    send_url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token='

    send_url += token

    d = dict(touser=userid, msgtype='text', text=dict(content=msg))

    body = json.dumps(d, indent=4)
    print(body)

    req2 = requests.post(send_url, json=body)
    jj = req2.content.decode(encoding='utf-8')
    print(jj)


def send_template_msg(token, userid, price, swing, swingrange):
    send_url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='

    send_url += token

    data = {'price':{'value':price,'color':'#173177'},
            'swing': {'value': swing, 'color': '#173177'},
            'swingrange': {'value': swingrange, 'color': '#173177'}
            }

    d = {'touser': userid,
         'template_id': Template_id,
         'url': 'http://www.dyhjw.com/hjtd/',
         'topcolor':'#FF0000',
         'data':data
         }

    body = json.dumps(d, indent=4)
    print(body)

    req2 = requests.post(send_url, body)
    jj = req2.content.decode(encoding='utf-8')
    print(jj)

def get_users(token):
    user_url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='
    user_url += token

    req3 = requests.get(user_url)
    jj = req3.content.decode(encoding='utf-8')
    print(jj)


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

    # reg1 = '<font>(.*?)</font></li>'
    # k = (re.findall(reg1, req, re.S))
    
    return key



if __name__ == '__main__':
    access_token = get_access_token(App_id, App_secret)
    # access_token = '_laZISLWl8fdCphcMzp66rUGas2KVu8NiqeztRYviLMR1L0FRRrLKel3WFmzJIYSlTJaZsActOgOd9G6zv21mc59GgES884viUFKUPxx_de1rJH0nNTrNllm0GYVTdQdTFTgABAZLZ'

    # send_text_msg(access_token, Open_id, 'hello')

    p = gold_price()

    send_template_msg(access_token, Open_id, p[0], p[1], p[2])
    send_template_msg(access_token, Open_id2, p[0], p[1], p[2])
    
    # get_users(access_token)



