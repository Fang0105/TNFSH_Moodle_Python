#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:44:03 2021

@author: student
"""

m=int(input())
if m>10000:
    print("Sleeping in school")
else:
    if m<=1500:
        print(70)
    else:
        m-=1500
        if m%500==0:
            print(70+(m//500)*5)
        else:
            print(70+(m//500)*5+5)
            