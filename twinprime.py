# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 03:41:01 2018

@author: Windows
"""

def prime(num):
    if num % 2 == 0:
        return False
    else:
        for i in range (3,num//2):
           if num % i == 0:
                return False
        return True

def twin_pair (val):
    for i in range (3,val,2):
        p = prime (i)
        q = prime (i+2)
        if p and q:
            print ('[' + str(i) + ',' + str(i+2) +']')


x = int (input("enter a number  :  "))
twin_pair(x)