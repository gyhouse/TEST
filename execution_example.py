#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:30:29 2023

@author: pablo
"""



a= 5

confirm= True

print(a)



b = "Hello Pablo"



list1=[1,2,3,4,5]

def function_sum_list(lis, val):
    res=[]
    for l in lis:
        l=l+val
        res.append(l)
    return res
    



val=1
list1= function_sum_list(list1, val)
print(list1)