#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:37:26 2021

@author: student
"""

n=int(input())
tot=0
flag = False
for i in range(2,n):
    if n%i==0:
        tot+=i
        flag=True
if flag==False:
    print("XD")
else:
    print(tot)