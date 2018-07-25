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

from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stops = stopwords.words('english')
papers=['wsj', 'npr', 'msnbc', 'blaze',  'nyt', 'fox', 'breitbart', 'huffpo', 'nation', 'inforwars']
paper = 'allpapers'

def makedf(paper):
    df = pd.read_csv('articles/'+paper+'.csv', names=['aid', 'paper', 'author', 'date', 'url', 'content'])
    #remove other types of shots
    badwords = ['flu', 'Russia', 'nuclear', 'Korea', 'Turkey']
    for word in badwords:
        df = df[df.content.str.contains(word) ==False]
    return df

wordnet_lemmatizer = WordNetLemmatizer()

def my_tokenizer(s):
    s =s.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) >2]
    tokens = [t for t in tokens if t not in stops]
    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
    return tokens

mydf = makedf(paper)

tokenized=[]
for k,v in mydf.iterrows():
    tok = (v['content'])
    tokens = my_tokenizer(tok)
    tokenized.append(str(tokens))


mydf['clean_content']=tokenized

ofile=open('cleandataset.csv', 'w')
mydf.to_csv(ofile)



numtops=24

""" Topic modelling using NMF"""
tfidf_vectorizer = TfidfVectorizer(max_df = 0.9, min_df = .1, stop_words=stops)
tfidf = tfidf_vectorizer.fit_transform(mydf['clean_content'])
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
nmf = NMF(n_components = numtops, random_state = 1, alpha = .1).fit(tfidf)


def get_top_words(model, feature_names, n_top_words, paper):
    topiclist=[]
    csvfile = open('topics/'+paper+str(numtops)+'.csv', 'w')
    w = csv.writer(csvfile)
    w.writerow(['topicID', 'topics'])
    for topic_idx, topic in enumerate(model.components_):
        tops = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        topiclist.append((topic_idx, tops))
    for tup in topiclist:
        w.writerow(tup)
    return topiclist

transformed_data = nmf.transform(tfidf)

topiclist = get_top_words(nmf, tfidf_feature_names, 10, paper)
    
transdata = pd.DataFrame(transformed_data)
transdata['paper']=mydf['paper']
transdata['aid']=mydf['aid']


outfile=open('topics-quantified_revised'+str(numtops)+'.csv', 'w')
transdata.to_csv(outfile)

outfile2=open('topics_list_revised'+str(numtops)+'.csv', 'w')
csv_out=csv.writer(outfile2)
for row in topiclist:
    csv_out.writerow(row)
    
outfile.close()
outfile2.close()

