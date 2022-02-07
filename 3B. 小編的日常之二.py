#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:35:42 2021

@author: student
"""
"""
str=input()
str=str.capitalize()
str=str.replace("She", "I")
str=str.replace("He", "I")
str=str.replace("does", "did")
str=str.replace("do", "did")
str=str.replace("have", "had")
str=str.replace("has", "had")
str=str.replace(".", "!")
str=str.capitalize()
print(str)
"""
str=input()
str=str.lower()
arr=str.split()
isFirst=True
for s in arr:
    if s=="he" or s=="she":
        print("I",end="")
    elif s=="does" or s=="do":
        print(" did",end="")
    elif s=="has" or s=="have":
        print(" had",end="")
    elif s[-1]=="." or s[-1]=="!":
        print(" ",end="")
        print(s[0:-1],end="")
        print("!")
    else:
        print(" ",end="")
        print(s,end="")
        