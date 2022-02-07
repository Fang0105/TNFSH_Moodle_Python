#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:33:27 2021

@author: student
"""

arr = input().split()

tot = 0.0
er = False
try:
    tot += float(arr[1])
except:
    print("Score 1 error!!")
    er = True  
try:
    tot += float(arr[2])
except:
    print("Score 2 error!!")
    er = True
    
if er==False:
    print('{0}: {1:.4f}'.format(arr[0], tot/2.0))
