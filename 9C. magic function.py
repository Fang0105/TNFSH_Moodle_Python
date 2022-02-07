#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:50:32 2021

@author: student
"""

def magic(n):
    if n==0:
        return 0
    else:
        sum=0.0
        for i in range(1,n+1):
            sum+=(1/i)
        return sum