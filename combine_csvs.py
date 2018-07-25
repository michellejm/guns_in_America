#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:39:59 2018

@author: mam
"""

import csv

papers=['wsj', 'npr', 'msnbc', 'blaze',  'nyt', 'fox', 'breitbart', 'huffpo', 'nation', 'inforwars']

fout=open("articles/allpapers.csv", "a")
for paper in papers:
    for line in open("articles/"+paper+".csv"):
         fout.write(line)  
fout.close()
         
fin = open("articles/allpapers.csv","r")
print(sum(1 for line in csv.reader(fin)))


