#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:13:36 2021

@author: student
"""

import math
a=float(input())
b=float(input())
c=float(input())
a1=((-1.0)*b+math.sqrt(b*b-4.0*a*c))/(2.0*a)
a2=((-1.0)*b-math.sqrt(b*b-4.0*a*c))/(2.0*a)
print('{0:.2f}\n{1:.2f}'.format(a1,a2))