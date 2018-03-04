#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:44:30 2018

@author: mam
"""

import shelve

db = shelve.open('wsjdb')

print(len(db))