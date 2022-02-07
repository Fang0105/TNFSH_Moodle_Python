#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:28:33 2021

@author: student
"""

str=input()
str=str.replace(':', ' ')
str=str.replace('.', ' ')
str=str.replace(',', ' ')
str=str.replace('?', ' ')
str=str.replace(';', ' ')
str=str.replace('"', ' ')
str=str.lower()
str=str.split()
dic={}
se=set()
for i in str:
    if (i in se)==True:    
        dic[i]+=1
    else:
        se.add(i)
        dic[i] = 1
arr=sorted(dic.keys())
for i in arr:
    print(i,': ',dic[i],sep='')
