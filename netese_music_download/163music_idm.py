import requests
import hashlib
import subprocess
import time
import json
import base64


headers = {
    'Cookie': 'os=uwp; osver=10.0.10586.318; appver=1.2.1;',
    'Referer': 'http://music.163.com/'
}


# 加密歌曲ID
def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2'.encode())
    byte2 = bytearray(id.encode())
    byte1_len = len(byte1)
    for i in range(len(byte2)):
        byte2[i] = byte2[i] ^ byte1[i % byte1_len]
    m = hashlib.md5()
    m.update(byte2)
    result = base64.urlsafe_b64encode(m.digest())
    return result.decode('utf-8')


# 获取歌曲的下载地址
# http://m1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# http://p1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# [song_dfsId]          为歌曲id，不同比特率有不同的id
# [encrypted_song_id]   为song_dfsId加密后的字符串
def get_mp3url(i):
    dl_url = 'http://p1.music.126.net/{}/{}.mp3'
    for q in ('hMusic', 'mMusic', 'lMusic'):
        if i[q]:
            dfsId = str(i[q]['id'])
            edfsId = encrypted_id(dfsId)
            mp3url = dl_url.format(edfsId, dfsId)
            return mp3url
    return None


# 歌单API
# POST http://music.163.com/weapi/v3/playlist/detail?csrf_token=
def get_playlist(playlist_id):
    api = 'http://music.163.com/weapi/v3/playlist/detail?csrf_token='

    params = {"id": playlist_id}

    songs_json = requests.post(api, para).json()

    songs_list = songs_json['result']['tracks']

    print('>> 歌单中共有{}首歌曲...'.format(len(songs_list)))

    song_infos = []
    for song in songs_list:
        song_info = dict(song_id=song['id'],
                         song_name=song['name'],
                         artist_name=song['artists'][0]['name'],
                         mp3url=get_mp3url(song))
        song_infos.append(song_info)
        print('{} {}'.format(song_info['artist_name'], song_info['song_name']))
        print(song_info['mp3url'])
    return song_infos


# 用IDM下载歌单中的歌曲，download songs in playlist by idm
# ID            为歌单id
# idm_dir       为IDM安装路径
# IDM cmdline   idman /d URL [/p localdir] [/f filename] [/q] [/h] [/n] [/a]
# /d URL        为下载链接
# /p localdir   定义要保存的文件放在哪个本地路径
# /f filename   定义要保存的文件到本地的文件名
# /a            添加一个指定的文件到下载队列，但是不开始下载
def download_playlist(id):
    idm_dir = u'C:\Program Files\Internet Download Manager\idman.exe'
    song_infos = get_song_infos(id)
    for i in song_infos:
        mp3url = i['mp3url']
        filename = '%s - %s.mp3' % (i['artist_name'], i['song_name'])
        cmd = '%s /a /d \"%s\" /f \"%s\"' % (idm_dir, mp3url, filename)
        print(cmd)
        cmd = cmd.encode('gbk')
        subprocess.Popen(cmd)
        time.sleep(0.5)


def main():
    # my playlist id
    playlistid = '459747'

    get_song_infos(playlistid)

    id ='1012650209189889'
    eid = encrypted_id(id)

    print(eid)

    dl_url = 'http://p1.music.126.net/{}/{}.mp3'

    print(dl_url.format(eid, id))

    # download_playlist(playlistid)


if __name__ == '__main__':
    main()
