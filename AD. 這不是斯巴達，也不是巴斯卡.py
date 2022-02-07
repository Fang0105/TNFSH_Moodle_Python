#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:54:32 2021

@author: student
"""

def fun(arr):
    if len(arr)==1:
        print(arr[0])
    else:
        tem=[]
        for i in range(0,len(arr)-1):
            tem.append(arr[i]+arr[i+1])
        fun(tem)
        for i in range(0,len(arr)):
            if i!=0:
                print(' ',end='')
            print(arr[i],end='')
        print()
    


str=input().split()
arr=[]
for i in str:
    arr.append(int(i))
fun(arr)