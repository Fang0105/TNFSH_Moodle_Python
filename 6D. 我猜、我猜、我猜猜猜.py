#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:53:13 2021

@author: student
"""

str=input().split()


l=int(str[0])
r=int(str[1])
goal=int(str[2])
cnt=1

while True:
    mid=(l+r)//2
    print('{0}: {1}'.format(cnt,mid))
    if mid<goal:
        l=mid+1
    elif mid>goal:
        r=mid-1
    else:
        break
    cnt+=1
        