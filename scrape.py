#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:31:32 2018

@author: mam
"""

import bs4
import requests

r = requests.get('http://www.breitbart.com/big-government/2018/02/26/parkland-shooting-survivor-vows-not-return-school-unless-gop-passes-gun-control/')
mypage = r.text
mysoup = bs4.BeautifulSoup(mypage)
comments = mysoup.find_all("section", {id:"conversation"})


print(comments)