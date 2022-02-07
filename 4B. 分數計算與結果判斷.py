#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:34:53 2021

@author: student
"""

a=float(input())
b=float(input())
c=float(input())
avg=(a+b+c)/3.0
if avg>100.0 or avg<0.0:
    print("BS")
elif avg>=60.0:
    print("PASS")
else:
    print("FAIL")