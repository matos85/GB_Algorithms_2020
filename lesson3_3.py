'''
 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

'''

import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

print(mass)

minimum = mass[0]
maksim = mass[0]
for i, x in enumerate(mass, 1):
    if x < minimum:
        minimum = x
    if x > maksim:
        maksim = x

print(minimum)
print(maksim)

for i in range(len(mass)):
    if mass[i] == minimum:
        minimum, maksim = maksim, minimum
    if mass[i] == maksim:
        mass[i] = minimum

print(mass)
