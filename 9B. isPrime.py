#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:50:32 2021

@author: student
"""

def isPrime(a):
    prime = True
    for i in range(2,a):
        if a%i==0:
            prime = False
            break
    return prime
