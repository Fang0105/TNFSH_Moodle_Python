#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:12:34 2021

@author: student
"""

str=input().split()
tar=input()
num=int(input())
cnt=0
isFirst=True
for i in str:
    if i==tar:
        cnt+=1
    if cnt==num:
        cnt+=1
    else:
        if isFirst==True:
            isFirst = False
        else:
            print(' ',end='')
        print(i,end='')
print()