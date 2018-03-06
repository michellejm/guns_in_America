#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:44:30 2018

@author: mam
"""

import shelve
import csv


db = shelve.open('breitbartdb')
print(len(db))
mykeys=list(db.keys())

with open('breitbart.csv', 'w') as csvfile:
    w = csv.writer(csvfile)
    for k in mykeys:
        key = db[k]
        author = str(key.author)
        date = key.date
        link = key.link
        content = key.text
        w.writerow([key, author, date, link, content])
    
#def paperdf(artids, authors, dates, urls, texts):
#    df = pd.DataFrame({'artid':artids, 'author':authors, 'date':dates, 'url':urls, 'text':texts})
#    return df





#import psycopg2

#connection = "dbname=newsdb user = mam"
#conn = psycopg2.connect(connection)
#cursor = conn.cursor()
    
#a = 157

#for key in mykeys:
#    key = db[key]
#    a+=1
#    author = key.author
#    date = key.date
#    link = key.link
#    content = key.text
#    query = "INSERT INTO sources (id, author, date, link, content) VALUES (%s, %s, %s, %s, %s);"
#    data = (a, author, date, link, content)
#    
#    cursor.execute(query, data)
#
#conn.commit()
    



