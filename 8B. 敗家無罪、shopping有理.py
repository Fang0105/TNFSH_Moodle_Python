#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:07:25 2021

@author: student
"""

str=input().split(',')
mx=0
mxitem=''
sum=0
for i in str:
    k=i.split(':')[0]
    y=i.split(':')[1]
    if mx<int(y):
        mxitem=k
        mx=max(mx,int(y))
    sum+=int(y)
    print(k,':',y)
print('Sum :',sum)
print('Top :',mxitem)