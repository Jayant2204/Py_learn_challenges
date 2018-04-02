# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 03:16:47 2018

@author: Windows
"""

def prime(num):
    if num % 2 == 0:
        return 1
    else:
        for i in range (3,num//2):
           if num % i == 0:
                return 1
        return 0

x = int (input("enter a number  :  "))
number = prime (x)          
print (str(x) + " is " + 'not'*(number) + " prime")