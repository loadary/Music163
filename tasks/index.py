#!/usr/bin/env python
# coding:utf-8

import requests
from lxml import etree
import urlparse
from __init__ import app


@app.task(ignore_result=True)
def index(url='http://music.163.com/discover'):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 DOL/s_1511_r2x9ak474125_821',
    }
    try:
        r = requests.get(url, headers=headers, timeout=4)
        html = etree.HTML(r.content)
        play_lists = [urlparse.urljoin('http://music.163.com/', link) for link in
                      html.xpath('//*[@id="discover-module"]/div[1]/div/div/div[1]/ul//li/div/a/@href') if
                      link.startswith('/playlist')]
        for url in play_lists:
            app.send_task(
                'tasks.playlist.playlist',
                args=(url, ),
                queue='playlist_queue',
                routing_key='tasks_playlist'
            )
    except:
        print '连接超时'