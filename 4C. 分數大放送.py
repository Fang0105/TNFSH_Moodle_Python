#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:39:28 2021

@author: student
"""

a=float(input())
b=float(input())
c=float(input())
if a<60:
    a*=1.25
if b<60:
    b*=1.25
if c<60:
    c*=1.25
avg=(a+b+c)/3
if avg>=60:
    print("Hmm")
else:
    print("PleaseGoToDieOneDie")