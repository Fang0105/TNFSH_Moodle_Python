#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:21:15 2021

@author: student
"""
arr=[]
try:
    while True:
        str=input().split(',')
        arr.append(set(str))
except:
    se=arr[0]
    se2=arr[0]
    for i in arr:
        se = se&i
        se2 = se2|i
    print(len(se))
    print(sorted(list(se2)))