#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:41:58 2018

@author: mam
"""

import nltk
import pandas as pd
import numpy as np
import csv


from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

papers=['fox', 'wsj', 'breitbart', 'inforwars', 'blaze', 'nyt', 'npr', 'huffpo', 'atlantic', 'msnbc']

paper = 'allpapers'
numtops=40



def makedf(paper):
    badwords = ['flu', 'Russia', 'nuclear', 'Korea', 'Turkey']
    df = pd.read_csv('artc/'+paper+'.csv', names=['aid', 'author', 'date', 'url', 'content'])
    df['paper']=np.where(df.aid.str.contains('fox|wsj|breitbart|inforwars|blaze|nyt|npr|huffpo|atlantic|msnbc'), df.aid.str[:3], 'other')
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


mydf = makedf(paper)

tokenized=[]
for k,v in mydf.iterrows():
    tok = (v['content'])
    tokens = my_tokenizer(tok)
    tokenized.append(str(tokens))

print(len(tokenized), "articles")
mydf['clean_content']=tokenized

tfidf_vectorizer = TfidfVectorizer(max_df = 0.3, min_df = 20, stop_words=stops)
tfidf = tfidf_vectorizer.fit_transform(mydf['clean_content'])
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
nmf = NMF(n_components = numtops, random_state = 1, alpha = .1).fit(tfidf)

topiclist=[]
def get_top_words(model, feature_names, n_top_words, paper):
    csvfile = open('topics/'+paper+'topics'+str(numtops)+'.csv', 'w')
    w = csv.writer(csvfile)
    w.writerow(['topicID', 'topics'])
    for topic_idx, topic in enumerate(model.components_):
        tops = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        topiclist.append((topic_idx, tops))
    for tup in topiclist:
        w.writerow(tup)
    return topiclist


transformed_data = nmf.transform(tfidf)

print(get_top_words(nmf, tfidf_feature_names, 7, paper))

    
transdata = pd.DataFrame(transformed_data)
transdata['paper']=mydf['paper']
transdata['artid']=mydf['aid']

print(type(transdata))


outfile=open('topics-quantified.csv', 'w')
transdata.to_csv(outfile)
