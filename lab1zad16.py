# -*- coding: cp1251 -*-
"""
Created on Sun Mar 12 20:17:55 2017

@author: energ
"""

import random 
import itertools 
import time
#from datetime import datetime #date for shedule
from datetime import datetime, timedelta

TeamList = [
        '«Реал Мадрид»-Испания',
	'«Манчестер Юнайтед»-Англия',
	'«ЦСКА»-Россия',
	'«Шахтёр»-ДНР',
	'«Спартак»-Россия',	
	'«Днепр»-Украина',	
	'«Ювентус»-Италия',	
	'«Милан»-Италия',
	'«Ливерпуль»-Англия'	,
	'«Ботафого»-Бразилия',	
	'«Бенфика»-Португалия',	
	'«Индепендьенте»-Аргентина',	
	'«Бока Хуниорс»-Аргентина',	
	'«Интернационале»-Италия',
	'«Арсенал»-Англия',
    '«Арсенал»-Россия'
    
    ]


random.shuffle(TeamList) #randomize spiska
print ('\n     Команды: ')
print ('\n'.join(TeamList))
 
TeamListGroup = [TeamList[i:i+4] for i in range(0, len(TeamList), 4)]#групировка по 4 #range(старт, стоп, шаг)

print ('\n Жеребьевка')
print ('Group A: ',TeamListGroup[0])
print ('Group B: ',TeamListGroup[1])
print ('Group C: ',TeamListGroup[2])
print ('Group D: ',TeamListGroup[3])
print ('\n Расписание матчей')

#-------date----------
tempDate = "14.09.2017"
#startDate = datetime.datetime.strptime(tempDate, "%d.%m.%Y")
startTime = [14,9,2017]
endTime = [14,4,2018]

print ('Season starts in', str(startTime[0])+'/'+str(startTime[1])+'/'+str(startTime[2])+' '+ str('22:45') )
print ('Season ends in', str(endTime[0])+'/'+str(endTime[1])+'/'+str(endTime[2])+' '+ str('22:45') )
now_date = datetime.now()
now_date = now_date.replace(2017,9,14)
print ('\n')


#---------------------
a = datetime(2017, 9, 20)
b = timedelta(days=14)#+2 недели
i=0
x=0
#print ('%s/%s/%s' % (now.month, now.day, now.year))
#print (str(a.day, a.month, a.year))
#print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45')
#print (str(a+b))
while a<=datetime(2018, 4, 14):# season end
    a=a+b # + 14 days
    if (x<15):
        print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[i]) +'  &  '+ str(TeamList[x+1] ) )
        i=i+1
        x=x+1
    else:
        print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ')