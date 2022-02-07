#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:55:39 2021

@author: student
"""

a=input()
try:
    sc=int(a)
    if sc>100 or sc<0:
        print("Error!")
    else:
        if sc>=90:
            print("Level A.")
            print("Work hard play hard.")
        elif sc>=80:
            print("Level B.")
            print("Work hard play hard.")
        elif sc>=70:
            print("Level C.")
            print("Work hard play hard.")
        elif sc>=60:
            print("Level D.")
            print("Work hard play hard.")
        else:
            print("Level E.")
            print("Play hard die hard.")
            
except:
    print("-_-")