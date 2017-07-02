#!/usr/bin/env python
# coding:utf-8

import time
import json
import requests
from libs.data import data
from libs.utils import store2db
from database.tables import Comment

from __init__ import app


@app.task(ignore_result=True)
def comment(url, song_id):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/song?id=430208269',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 DOL/s_1511_r2x9ak474125_821',
    }
    try:
        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 200:
            cont = json.loads(r.content)
            if cont['code'] == 200:
                hotComments = cont['hotComments']
                for comment in hotComments:
                    res = {}
                    res['userId'] = comment['user']['userId']
                    res['nickname'] = comment['user']['nickname']
                    res['avatarUrl'] = comment['user']['avatarUrl']
                    res['content'] = comment['content']
                    res['likedCount'] = comment['likedCount']
                    res['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(comment['time']/1000))
                    res['song_id'] = song_id
                    store2db(Comment, res)
    except:
        pass


if __name__ == '__main__':
    # home_page()
    comment()