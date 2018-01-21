# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:14:29 2018

@author: Sanidhya
"""
import numpy as np

x = np.array([2,1,5,6,3,4,0])
print(np.sort(x)) # to sort the arrays 
print(np.argsort(x)) # to return the index of sorted elements 
i = x.argsort() # to return index of sorted elements 
print(x[i]) # to print sorted array using a fancy indexing

#Sorting along rows and coloumns 

x= np.random.RandomState(42).randint(0,10,(4,6))
print(np.sort(x,axis=0)) # sorting along axis 0 of matrix
print(np.sort(x,axis=1)) #sorting along axis 1 of matrix
