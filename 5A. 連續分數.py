#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:22:39 2021

@author: student
"""

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += (1/i)
print('{0:.4f}'.format(sum))