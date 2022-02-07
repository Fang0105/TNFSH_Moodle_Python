#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:59:53 2021

@author: student
"""
a=input().split(' ')

name=a[0]
print(a[0]+':',end="")

#avg=(float(a[1])+float(a[2])+float(a[3])+float(a[4])+float(a[5]))/5
sum=0.0
for i in range(1,6):
   sum+=float(a[i]) 
avg=sum/5
print("{0:.4f} ".format(avg))
