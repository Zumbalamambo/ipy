#!/usr/bin/env python2
# vim: set file encoding=gbk

import requests
import md5
import subprocess
import time

# ���ܸ���ID
def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result

# ��ȡ���������ص�ַ
# http://m1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# http://p1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# [song_dfsId]          Ϊ����id����ͬ�������в�ͬ��id
# [encrypted_song_id]   Ϊsong_dfsId���ܺ���ַ���
def get_mp3url(i):
    for q in ('hMusic', 'mMusic', 'lMusic'):
        if i[q]:
            dfsId = str(i[q]['dfsId'])
            edfsId = encrypted_id(dfsId)
            mp3url = u'http://p1.music.126.net/%s/%s.mp3' % (edfsId, dfsId)
            return mp3url
    return None

# ��ȡ�赥������и�����Ϣ
# http://music.163.com/api/playlist/detail?id=[playlist_id]"
# [playlist_id]     Ϊ�赥id
def get_song_infos(id):
    url_playlist = "http://music.163.com/api/playlist/detail?id=%s"

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml; " \
            "q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"text/html",
        "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"http://music.163.com/",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) " \
            "AppleWebKit/537.36 (KHTML, like Gecko) " \
            "Chrome/40.0.2214.91 Safari/537.36"
    }
    ss = requests.session()
    ss.headers.update(headers)

    songs_json = ss.get(url_playlist % id).json()
    songs_list = songs_json['result']['tracks']
    print u'>> �赥�й���%s�׸���.' % len(songs_list)

    song_infos = []
    for i in songs_list:
        song_info = {}
        song_info['song_id'] = i['id']
        song_info['song_name'] = i['name']
        song_info['artist_name'] = i['artists'][0]['name']
        song_info['mp3url'] = get_mp3url(i)
        song_infos.append(song_info)
        print u'%s %s' % (song_info['artist_name'], song_info['song_name'])
        print song_info['mp3url']
    return song_infos

# ��IDM���ظ赥�еĸ�����download songs in playlist by idm
# ID            Ϊ�赥id
# idm_dir       ΪIDM��װ·��
# IDM cmdline   idman /d URL [/p localdir] [/f filename] [/q] [/h] [/n] [/a]
# /d URL        Ϊ��������
# /p localdir   ����Ҫ������ļ������ĸ�����·��
# /f filename   ����Ҫ������ļ������ص��ļ���
# /a            ���һ��ָ�����ļ������ض��У����ǲ���ʼ����
def download_playlist(id):
    idm_dir = u'C:\Program Files\Internet Download Manager\idman.exe'
    song_infos = get_song_infos(id)
    for i in song_infos:
        mp3url = i['mp3url']
        filename = '%s - %s.mp3' % (i['artist_name'], i['song_name'])
        cmd = '%s /a /d \"%s\" /f \"%s\"' % (idm_dir, mp3url, filename)
        print cmd
        cmd = cmd.encode('gbk')
        subprocess.Popen(cmd)
        time.sleep(0.5)

def main():
    # my playlist id
    playlistid = u'483762036'
    download_playlist(playlistid)

if __name__ == '__main__':
    main()







