# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:20:46 2021

@author: dingrongmei
"""

import numpy as np
data = {
     'zhangfei':[68, 65, 30],
     'guanyu': [95, 76, 98],
     'liubei': [98,86,88],
     'dianwei': [90, 88, 77],
     'xuchu': [80, 90, 90]
     }

chinese = []
math = []
english = []

for key, value in data.items():
    #print(key, value)
    chinese.append(value[0])
    math.append(value[1])
    english.append(value[2])
    sum_value = np.sum(data[key])
    data[key].append(sum_value)
    #print(data[key])
    
mean_ch = np.mean(chinese) #average score
mean_math = np.mean(math)
mean_eng = np.mean(english)
print ('chinese average: ', mean_ch)
print ('math average: ', mean_math)
print ('english average: ', mean_eng)

std_ch = np.std(chinese) # standard 
std_math = np.std(math)
std_eng = np.std(english)
print ('chinese standard: ', std_ch)
print ('math standard: ', std_math)
print ('english standard: ', std_eng)

var_ch = np.var(chinese) # var 
var_math = np.var(math)
var_eng = np.var(english)
print ('chinese var: ', var_ch)
print ('math var: ', var_math)
print ('english var: ', var_eng)

min_ch = np.min(chinese)  #minmum
min_math = np.min(math)
min_eng = np.min(english)
print ('chinese min: ', min_ch)
print ('math min: ', min_math)
print ('english min: ', min_eng)

max_ch = np.max(chinese) # max
max_math = np.max(math)
max_eng = np.max(english)
print ('chinese max: ', max_ch)
print ('math max: ', max_math)
print ('english max: ', max_eng)

ordered_data = sorted(data.items(), key=lambda d: d[1][3], reverse=True)

print(ordered_data)