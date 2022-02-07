#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:26:47 2021

@author: student
"""

str=input().split()
m=int(str[0])
n=int(str[1])
str=input().split()
x=int(str[0])
y=int(str[1])
tot=m*n
cnt=0
arr=[]
for i in range(m):
   tem=[]
   for j in range(n):
       tem.append(0)
   arr.append(tem)
str=input().split()
for i in str:
    if arr[x][y]==0:
        cnt+=1
    arr[x][y]+=1
    if cnt==tot:
        break
    if i=='1':
        x-=1
    elif i=='2':
        y+=1
    elif i=='3':
        x+=1
    else:
        y-=1
    if x<0:
        x=0
    if x==m:
        x=m-1
    if y<0:
        y=0
    if y==n:
        y=n-1
walk=0
for i in arr:
    for j in i:
        walk+=j
print(walk)