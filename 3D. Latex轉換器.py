#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:29:44 2021

@author: student
"""

str=input()
arr=str.split()
isfirst=True
for s in arr:
    ss=s[0:5]
    if isfirst==True:
        isfirst = False
    else:
        print(" ",end="")
    if ss=="sqrt(":
        print('$\sqrt{',end="")
        print(s[5:-1],end="")
        print("}$",end="")
    else:
        print(s,end="")