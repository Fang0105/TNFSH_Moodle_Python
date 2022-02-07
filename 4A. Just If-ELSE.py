#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:14:59 2021

@author: student
"""

a=int(input())
if a==0:
    print("Z")
elif a>0:
    if a%2==0:
        print("E")
    else:
        print("O")
else:
    print("M")