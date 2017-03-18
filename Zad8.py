# -*- coding: cp1251 -*-


from random import randint
from math import log

RandomNumbers = []

RandMaxNumber = int(input('Введите размер массива\n'))

for i in range(1<<int(round(log(RandMaxNumber,2)))):

    if i <= RandMaxNumber:

        RandomNumbers.append(randint(1, 10000))
        
    else:
        
        RandomNumbers.append(0)#заполняем нулями

print('Случайные числа')

print(' '.join(str(RandomNumbers)))

print('Количество элементов в списке {}'.format(len(RandomNumbers)))

#print('Отдельное случайное число - {}'.format(randint(1, 10000)))
