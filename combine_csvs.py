#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:39:59 2018

@author: mam
"""

import csv

papers=['wsj', 'npr', 'msnbc', 'blaze',  'nyt', 'fox', 'breitbart', 'huffpo', 'nation', 'inforwars']

libpapers=['npr', 'msnbc', 'nyt', 'huffpo', 'nation' ]
conspapers = ['blaze', 'wsj', 'fox', 'breitbart', 'inforwars']


#fout=open("articles/allpapers.csv", "a")
#for paper in papers:
#    for line in open("articles/"+paper+".csv"):
#         fout.write(line)  
#fout.close()

fout_l=open("articles/libpapers.csv", "a")
for paper in libpapers:
    for line in open("articles/"+paper+".csv"):
         fout_l.write(line)  
fout_l.close()

fout_c=open("articles/conspapers.csv", "a")
for paper in conspapers:
    for line in open("articles/"+paper+".csv"):
         fout_c.write(line)  
fout_c.close()
         
fin = open("articles/allpapers.csv","r")
print(sum(1 for line in csv.reader(fin)))


