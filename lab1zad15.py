# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:16:55 2017

@author: energ
"""

def pre_process(a):
    def dec_process(fn):
        print (s)
        for i in range(len(s)):
            s[i] = s[i] - a*s[i-1] 
        print (s)
    return dec_process

s = [1.2,3.0,0.79]

@pre_process(a=0.93) 
def plot_signal(s):
    for sample in s:
       print(sample)