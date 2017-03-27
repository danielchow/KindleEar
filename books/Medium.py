#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Medium

class Medium(BaseFeedBook):
    title                 = u'Medium订阅'
    description           = u'推送我的Medium订阅'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 1
    oldest_article        = 2
    mastheadfile          = "mh_dapenti.gif"
    coverfile             = "cv_dapenti.jpg"
    network_timeout       = 60
    fetch_img_via_ssl     = False
    feeds = [
            (u'FreeCodeCamp', 'https://medium.freecodecamp.com/feed', True),
            (u'HackerNoon', 'https://hackernoon.com/feed', True),
            (u'AndroidPub', 'https://android.jlelse.eu/feed', True),
            (u'Backchannel', 'https://backchannel.com/feed', True),
           ]
    
    # def soupbeforeimage(self, soup):
    #     # 更换另一个图库，因为RSS中的图库已经被封
    #     for img in soup.find_all('img', attrs={'src':True}):
    #         if img['src'].startswith('http://ptimg.org:88'):
    #             img['src'] = img['src'].replace('http://ptimg.org:88','http://pic.yupoo.com')
