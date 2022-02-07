#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:26:11 2021

@author: student
"""

a=int(input())
b=int(input())
number = False
for i in range(a,b+1):
    if number==True:
        break;
    else:
        tot = 0
        for j in range(1,i):
            if i%j==0:
                tot+=j
        if tot==i:
            print(i)
            number = True
if number==False:
    print("No number is perfect")