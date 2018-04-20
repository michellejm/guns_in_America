#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:24:35 2018

@author: mam
"""

import csv
import pandas as pd
import numpy as np



df = pd.read_csv('topics-quantified.csv', header=0, index_col=0)
dftopics = pd.read_csv('topics/allpaperstopics30-coded.csv', header=0)

#fill in missing papers
df['paper'].fillna(method='ffill', inplace=True)

#find the average weight of each topic per paper
dfgrp=df.groupby('paper').mean()

#find the biggest topic for each paper
maxes=dfgrp.idxmax(axis=1)

#transpose that df
dft=dfgrp.T
dft['topicID']=list(range(0,30))

#join the topics to the dataframe
dfj=pd.merge(dft, dftopics, how='inner',on='topicID')
dfj.drop(['topicID'], axis=1, inplace=True)

#filter out topics that are below .01 in weight
#dfj=dfj[dfj>.01]


#dfj.plot(kind='bar')

#dfj=dfj[dfj['global']=='nra']
print(dfj)

outfile=open('alltopics-weights.csv', 'w')
dfj.to_csv(outfile)

