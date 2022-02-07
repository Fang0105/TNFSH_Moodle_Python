#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:40:58 2021

@author: student
"""

def fun(n):
    if n<0:
        return 0
    else:
        return fun(n-2)+n

n=int(input())
print(fun(n))