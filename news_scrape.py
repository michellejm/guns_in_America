#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:34:47 2018

@author: mam

This program first makes a list of article links and then follows those to 
get the related content.
"""

from newspaper import Article
from classtools import AttrDisplay
from googleapiclient.discovery import build

import shelve
import json


"""make a list of links for all the articles that have the keywords from a 
custom google search. It then follows each link and gets the author, date, and
text from the article, returning it as a python db.

TO USE: Set newspapers and word list at the bottom.
"""
def getService():
    service = build("customsearch", "v1",
            developerKey="AIzaSyC3bsWJ5I1dcA5Dqj3bVTTWtZo96lYwxvw")
    return service

def pagesearch(engineid, wordlist, paper):
    pageLimit = 10
    service = getService()
    startIndex = 1
    response = []

    for nPage in range(0, pageLimit):
        for word in wordlist:
            response.append(service.cse().list(
                q=word, #Search words
                cx=engineid,  #CSE Key
                #lr='lang_pt', #Search language
                start=startIndex
            ).execute())
    
            startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

    with open(paper+'data.json', 'w') as outfile:
        json.dump(response, outfile)

    outfile.close()

    data = json.load(open(paper+'data.json'))
    links=[]
    
    for obj in data:
        embedded = obj['items']
        for item in embedded:
            mylink = item['link']
            if mylink not in links:
                links.append(mylink)
            else:
                pass
            
    return links


class SavedArticles(AttrDisplay):
    def __init__(self, artid, author, date, link, text):
        self.artid = artid
        self.author = author
        self.date = date
        self.link = link
        self.text = text
    def wordCount(text):
        pass
    def keyWordCount(text):
        pass
    
    
def paperdb(links, paper):
    #use the results of the json file and find only the links.
    db = shelve.open(paper+'db')
    
    #Use the newspaper module to parse the articles
    for url in links:
        article = Article(url)
        article.download()
        article.parse()
        
        author = article.authors
        text = article.text
        date = article.publish_date
        
        artid = ('a'+ str(links.index(url)))
        artid = SavedArticles(artid, author, date, url, text)
        db[artid.artid] = artid
        
    db.close()


"""Make a Google Custom Search for each newspaper. Find the CSE ID under 
Basics > Details > Search Engine ID
"""

wordlist = ['gun', 'firearm', 'AR15', 'weapon', 'shot', 'rifle']

#Breitbart
paperbb = 'breitbart'
custom_search_id_bb = '010452994600902477721:jnqwe5bzppe'

#NYTimes (doesn't work)
papernyt='nyt'
custom_search_id_nyt = '010452994600902477721:_xacvksvdiy'

#Wall Street Journal
paperwsj='wsj'
custom_search_id_wsj = '010452994600902477721:lg-xm4efonu'

links = pagesearch(custom_search_id_wsj, wordlist, papernyt)
paperdb(links, paperwsj)





    

    
