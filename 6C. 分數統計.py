#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:41:27 2021

@author: student
"""
import math

arr=[]
passNum=0
failNum=0
tot=0.0
num=0
try:
    while True:
        n=float(input())
        arr.append(n)
        if n>=60.0:
            passNum+=1
        else:
            failNum+=1
        tot+=n
        num+=1   
except:
    avg=tot/num
    sigma=0.0
    for i in arr:
        sigma+=(i-avg)**2
    sigma=math.sqrt(sigma/num)
    print(passNum)
    print(failNum)
    print('{0:.2f}\n{1:.2f}\n'.format(avg, sigma))