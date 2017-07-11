#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import hashlib
import subprocess
import time


# 加密歌曲ID
def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in range(len(byte2)):
        byte2[i] = byte2[i] ^ byte1[i % byte1_len]
    m = hashlib.md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result


# 获取歌曲的下载地址
# http://m1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# http://p1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# [song_dfsId]          为歌曲id，不同比特率有不同的id
# [encrypted_song_id]   为song_dfsId加密后的字符串
def get_mp3url(i):
    for q in ('hMusic', 'mMusic', 'lMusic'):
        if i[q]:
            dfsId = str(i[q]['dfsId'])
            edfsId = encrypted_id(dfsId)
            mp3url = u'http://p1.music.126.net/%s/%s.mp3' % (edfsId, dfsId)
            return mp3url
    return None


# 获取歌单里的所有歌曲信息
# http://music.163.com/api/playlist/detail?id=[playlist_id]"
# [playlist_id]     为歌单id
def get_song_infos(id):
    url_playlist = "http://music.163.com/api/playlist/detail?id=%s"

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml; " \
                  "q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "text/html",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://music.163.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " \
                      "AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/40.0.2214.91 Safari/537.36"
    }
    ss = requests.session()
    ss.headers.update(headers)

    songs_json = ss.get(url_playlist % id).json()
    songs_list = songs_json['result']['tracks']
    print('>> 歌单中共有%s首歌曲.' % len(songs_list))

    song_infos = []
    for i in songs_list:
        song_info = dict(song_id=i['id'], song_name=i['name'], artist_name=i['artists'][0]['name'],
                         mp3url=get_mp3url(i))
        song_infos.append(song_info)
        print('%s %s' % (song_info['artist_name'], song_info['song_name']))
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
    playlistid = u'483762036'
    download_playlist(playlistid)


if __name__ == '__main__':
    main()
