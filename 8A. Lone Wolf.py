#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:03:01 2021

@author: student
"""

str=input().split()
se = set()
for i in str:
    if  (i in se) == True:
        se.remove(i)
    else:
        se.add(i)
for i in se:
    print(i)
