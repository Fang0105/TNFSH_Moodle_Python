#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:37:35 2021

@author: student
"""

str=input()
x=7
sum=0
for i in str:
    if i=="1":
        sum+=pow(2,x)
    x-=1
print('The value of binary {0} in decimal is is: {1}.'.format(str,sum))