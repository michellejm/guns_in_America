#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:39:59 2018

@author: mam
"""

import csv

papers=['fox', 'wsj', 'breitbart', 'inforwars', 'blaze', 'nyt', 'npr', 'huffpo', 'atlantic', 'msnbc']

fout=open("artc/allpapers.csv","a")
for paper in papers:
    for line in open("artc/"+paper+".csv"):
         fout.write(line)  
fout.close()
         
fin = open("artc/allpapers.csv","r")
print(sum(1 for line in csv.reader(fin)))


