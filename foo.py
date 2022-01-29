# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:13:10 2022

@author: kiteoki
"""

def is_divisible_by_k(x,k):
    '''
    Checks whether x is divisible by k.
    '''
    assert x%k==0
    

'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (incl. doubles)
'''

x=()
for i in range(1000):
    if (is_divisible_by_k(x,2) & is_divisible_by_k(x,3)) | is_divisible_by_k(x,7):
        x.append(i)
        
        
'''
Sum all the integers that are multiples of 2 or 5 or 6 that are lower or equal to 1000 (excl. doubles)
'''

sum(x)        