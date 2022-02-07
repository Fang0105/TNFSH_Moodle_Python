#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:50:32 2021

@author: student
"""

def resort(li):
    li2=[]
    cnt=0
    for i in li:
        if i=="0":
            cnt+=1
        else:
            li2.append(i)
    for i in range(0,cnt):
        li2.append("0")
    return li2