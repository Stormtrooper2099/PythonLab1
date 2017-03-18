# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:50:57 2017

@author: energ
"""

def get_frames(signal,size,overlap):
    
    print ('Step: ')
    x = signal
    step = size * overlap
    print (step)
    i = 0
    while i<len(signal):
        print (signal[i:i+size]) #ot 0 do stap, ot stap + size
        i = i + int(step)


size = 4     #razmer okna
signal = [i for i in range(0,10)] #razer signala
overlap = 0.5 #stepen perekritia


get_frames(signal,size,overlap)