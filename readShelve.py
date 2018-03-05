#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:44:30 2018

@author: mam
"""

import shelve

db = shelve.open('newsDatabases/wsjdb')

mykeys = list(db.keys())
for key in mykeys[:5]:
    print(db[key])