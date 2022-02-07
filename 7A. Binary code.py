#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:48:13 2021

@author: student
"""

n=int(input())
for i in range(n):
    str=input()
    if str=="0 1 0 1":
        print('A',end='')
    elif str=="0 1 1 1":
        print('B',end='')
    elif str=="0 0 1 0":
        print('C',end='')
    elif str=="1 1 0 1":
        print('D',end='')
    elif str=="1 0 0 0":
        print('E',end='')
    elif str=="1 1 0 0":
        print('F',end='')
print()