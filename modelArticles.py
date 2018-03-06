#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:58 2018

@author: mam
"""

import nltk
import pandas as pd
import numpy as np


from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans


def makedf(paper):
    badwords = ['flu', 'Russia', 'nuclear', 'Korea', 'Turkey']
    df = pd.read_csv('artc/'+paper+'.csv', names=['aid', 'author', 'date', 'url', 'content'])
    for word in badwords:
        df = df[df.content.str.contains(word) ==False]
    return df

stops = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()

def my_tokenizer(s):
    s =s.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) >2]
    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
    tokens = [t for t in tokens if t not in stops]
    return tokens


mydf = makedf('msnbc')


tokenized=[]
for k,v in mydf.iterrows():
    tok = (v['content'])
    tokens = my_tokenizer(tok)
    for t in tokens:
        tokenized.append(t)

print(len(tokenized))

tfidf_vectorizer = TfidfVectorizer(max_df = 0.3, min_df = 20, stop_words=stops)
tfidf = tfidf_vectorizer.fit_transform(tokenized)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
nmf = NMF(n_components = 10, random_state = 1, alpha = .1).fit(tfidf)

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


transformed_data = nmf.transform(tfidf)
len(transformed_data)

print_top_words(nmf, tfidf_feature_names, 20)

        


    
        
#
#if __name__ == "__main__":
#    mydf = makedf('breitbart')

    