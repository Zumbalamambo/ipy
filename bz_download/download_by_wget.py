#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wget
import time
import re

# http://m1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3
# http://p1.music.126.net/[encrypted_song_id]/[song_dfsId].mp3

# 用WGET下载歌单中的歌曲，download songs in playlist by wget
# ID    为歌单id
# WGET  wget.download(url, filename or directory)

url = input('input download url,plz...')

filename = "1.pdf"

wget.download(url, filename)
time.sleep(0.5)