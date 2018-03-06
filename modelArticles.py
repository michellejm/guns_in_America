#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:58 2018

@author: mam
"""

import nltk
import pandas as pd
import numpy as np
import shelve

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def makedf(paper):
    badwords = ['flu', 'Russia', 'nuclear', 'Korea', 'Turkey']
    df = pd.read_csv('artc/'+paper+'.csv', names=['aid', 'author', 'date', 'url', 'content'])
    for word in badwords:
        df = df[df.content.str.contains(word) ==False]
    return df
                
#wordnet_lemmatizer = WordNetLemmatizer()
#
#def my_lemmatizer(s):
#    s =s.lower()
#    tokens = nltk.tokenize.word_tokenize(s)
#    tokens = [t for t in tokens if len(t) >2]
#    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
#    tokens = [t for t in tokens if t not in stopwords.words('english')]
#    return tokens
#
#word_index_map = {}
#current_index = 0
#tokenized=[]
#
#for row in df:
#    tokens = my_tokenizer(df[])
#
#def article_compiler(art):
#    pass
    
        

if __name__ == "__main__":
    mydf = makedf('breitbart')
    for k,v in mydf.iterrows():
        print(v['content'])
    