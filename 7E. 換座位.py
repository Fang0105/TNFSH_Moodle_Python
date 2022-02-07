#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:01:42 2021

@author: student
"""

x=int((input().split())[0])
y=int((input().split())[0])
arr=[]
for i in range(x):
    arr.append(input().split())
for i in range(y-1,-1,-1):
    for j in range(x):
        #print(i,j)
        print('%3s'%arr[j][i],end='')
    print()