# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:49:02 2017

@author: energ
"""
import math

def frange(start,end,step):

    #func range

    st = int(start) #int start

    start = float(start)    #privedenie k float

    end = float(end)

    step = round(float(step),2) #okryglaem

    add = []    #init array

    add.append(start)   #addition elements to array

    endF = int(math.fabs(end-start)/step)   #polojitelnoe kol-vo shagov

    buf = range(st,endF)

    if (start > 0)&(end > 0):

        for i in buf: 

            add.append(add[i-1] + step)

            round(add[i-1],2)

        return add

    else:

        for i in buf:

            add.append(add[i-1] - step)

            round(add[i-1],2)

        return add

for y in frange(1, 5, 0.1):

    print (round(y,2))