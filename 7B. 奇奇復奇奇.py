#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:52:51 2021

@author: student
"""

str=input()
tot=0
cnt=0
for i in str:
    if cnt%2==0:
        tot+=int(i)
    else:
        tot-=int(i)
    cnt+=1
print(abs(tot))