'''
В одномерном массиве целых чисел определить два наименьших элемента.
 Они могут быть как равны между собой (оба являться минимальными), так и различаться.

'''

import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
# mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
mass = [8, 3, 2, 7, 8, -3, 9, 8, 8, 7, 7, 5, 8, 7, 6, 3, 8, -3, ]
print(mass)

res = []
a = 0

while a != 2:
    minimum = mass[0]
    for i in mass:
        if i < minimum:
            minimum = i
    res.append(minimum)
    mass.remove(minimum)
    a += 1
print(res)
