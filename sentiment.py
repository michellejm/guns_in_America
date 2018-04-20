#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:35:55 2018

@author: mam
"""
import csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import pandas as pd

df = pd.read_csv('topics-quantified.csv', header=0, index_col=0)

def sentanal(tokens):
    sents=[]
    for tok in tokens:
        blob=TextBlob(tok, analyzer=NaiveBayesAnalyzer())
        sents.append(blob.sentiment)
    return sents

#sentser=sentanal(df['clean_content'])

#df['sents']=sentser

print(df)