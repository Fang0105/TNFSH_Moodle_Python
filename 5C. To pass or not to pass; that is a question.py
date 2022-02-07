#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:05:29 2021

@author: student
"""

str=input().split()
passmn=100
failmx=0
arr=[]
for i in str:
    h=int(i)
    arr.append(h)
    if(h>=60):
        passmn = min(passmn,h)
    if(h<60):
        failmx = max(failmx,h)
        
arr.sort(reverse=True)
for i in range(len(arr)):
    if i!=0:
        print(" ",end="")
    print(arr[i],end="")
print()
if(failmx==0):
    print("best case")
else:  
     print(failmx)
if(passmn==100):
    print("worst case")
else:
    print(passmn)

     

