#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:08:56 2021

@author: student
"""

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum+=(1/i)
print('{0:.4f}'.format(sum))