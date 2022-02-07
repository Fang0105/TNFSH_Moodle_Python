#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:10:25 2021

@author: student
"""

while True:
    str=input().split()
    a=int(str[0])
    b=int(str[1])
    print('{0} {1} '.format(a,b),end='')
    if a>b:
        tem=a
        a=b
        b=tem
    mxlen=0
    for i in range(a,b+1):
        k=i
        temlen = 1
        while k!=1:
            temlen+=1
            if k%2==0:
                k/=2
            else:
                k=3*k+1
        mxlen=max(mxlen,temlen)
    print(mxlen)
        