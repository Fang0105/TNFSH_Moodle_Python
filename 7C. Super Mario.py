#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:55:11 2021

@author: student
"""

n=int(input())
str=input().split()
former=-1
high=0
low=0
for i in str:
    a=int(i)
    if former==-1:
        former=a
    else:
        if a>former:
            high+=1
        elif a<former:
            low+=1
        former=a
print(high)
print(low)