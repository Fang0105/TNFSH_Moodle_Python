#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:45:10 2021

@author: student
"""

ww=[123]
def fun(arr):
    sum=0
    for i in arr:
        if type(i)==type(ww):
            sum+=fun(i)
        else:
            sum+=int(i)
    return sum


str=input()
arr=eval(str)
print(fun(arr))