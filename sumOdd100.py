# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:18:39 2021

@author: dingrongmei
"""
import numpy as np

def sumOdd100():
    x = np.linspace(2, 100, num=50, dtype=np.int32)
    sum = np.sum(x)     
    return sum;
        
print(sumOdd100())

