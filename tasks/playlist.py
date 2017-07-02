#!/usr/bin/env python
# coding:utf-8

import time
import requests
from __init__ import app
from lxml import etree
from libs.utils import search


@app.task(ignore_result=True)
def playlist(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 DOL/s_1511_r2x9ak474125_821',
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = etree.HTML(r.content)
            ids = [search(link).group() for link in html.xpath('//a/@href') if link.startswith('/song?id') and search(link)]
            for song_id in ids:
                url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(song_id)
                app.send_task(
                    'tasks.comment.comment',
                    args=(url, song_id),
                    queue='comment_queue',
                    routing_key='tasks_comment'
                )
                time.sleep(5)
    except:
        print '连接超时'