#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:04:15 2021

@author: student
"""

import math
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2.0
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('{0:.2f}'.format(area))