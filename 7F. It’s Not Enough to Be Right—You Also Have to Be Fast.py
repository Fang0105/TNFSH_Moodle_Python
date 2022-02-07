#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:17:05 2021

@author: student
"""

str=input().split()
cnt=0
for i in str:
    if i=='0':
        cnt+=1
    else:
        print(i,end=' ')
for i in range(cnt):
    print('0',end=' ')
print()
    