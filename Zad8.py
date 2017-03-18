# -*- coding: cp1251 -*-


import random
n = int(random.uniform(0, 100))
print(n)

nArray = [random.randrange(0, 100) for i in range(n)]
print (nArray)

p = 2
i = 0
while p**i <= n:
    zero = p**i
    i = i + 1

zero = (p**i)
print('zero',zero)

appendix = zero - n
for i in range(appendix):
    nArray.append(0)

print(nArray)
