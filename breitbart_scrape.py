#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:34:47 2018

@author: mam

This program first makes a list of article links and then follows those to 
get the related content.
"""

from newspaper import Article
from googleapiclient.discovery import build

import urllib.request
import bs4
import json
import shelve

"""make a list of links for all the articles that have the keywords from a 
custom google search. This custom search only searches Breitbart.
It then saves the results in a json file
"""
def getService():
    service = build("customsearch", "v1",
            developerKey="AIzaSyC3bsWJ5I1dcA5Dqj3bVTTWtZo96lYwxvw")

    return service

def main():

    pageLimit = 10
    service = getService()
    startIndex = 1
    response = []
    wordlist=['gun', 'firearm', 'AR15', 'weapon', 'shot']

    for nPage in range(0, pageLimit):
        for word in wordlist:
            response.append(service.cse().list(
                q=word, #Search words
                cx='010452994600902477721:jnqwe5bzppe',  #CSE Key
                #lr='lang_pt', #Search language
                start=startIndex
            ).execute())
    
            startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

    with open('data.json', 'w') as outfile:
        json.dump(response, outfile)

main()

#use the results of the json file and find only the links.

data = json.load(open('data.json'))
links=[]

for obj in data:
    embedded = obj['items']
    for item in embedded:
        mylink = item['link']
        if mylink not in links:
            links.append(mylink)
        else:
            pass

class SavedArticles:
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
    
    
db = shelve.open('breitbartdb')

#Use the newspaper module to parse the articles
for url in links[:2]:
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

mydb = shelve.open('breitbartdb')

for key in mydb:
    print(key, ':', mydb[key])

    


    

    
