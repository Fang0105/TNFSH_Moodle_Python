#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:26:08 2021

@author: student
"""
import math
str=input().split()
n=len(str)
tot = 0.0
for i in str:
    tot+=float(i)
avg=(tot/n)
sigma=0.0
for i in str:
    sigma+=(int(i)-avg)**2
sigma=math.sqrt(sigma/n)
print('{0:.3f}'.format(sigma))

