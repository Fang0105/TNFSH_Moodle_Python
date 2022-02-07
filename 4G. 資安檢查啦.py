#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:06:01 2021

@author: student
"""

url=input()
if url.startswith("https://") and url.endswith("tn.edu.tw"):
    print("OK!!")
elif url.startswith("http://") and url.endswith("tnfsh.tn.edu.tw"):
    print("OK!!")
else:
    print("Invalid web site URL!")