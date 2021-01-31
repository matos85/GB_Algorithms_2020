'''
Задача из урока 3 номер задачи 4:

Определить, какое число в массиве встречается чаще всего.
'''

import timeit
import cProfile

# Версия 1 - оригинальная
t1 = '''
import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
res = [0, 0]

for i in range(len(mass)):
    c = 0
    z = mass[i]
    for k in mass:
        if z == k:
            c += 1
        if c > res[1]:
            res[0] = z
            res[1] = c
if res[1] == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {res[0]} встретилось {res[1]} раз')
'''
t2 = '''
import random

SIZE_N = 100
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
res = [0, 0]

for i in range(len(mass)):
    c = 0
    z = mass[i]
    for k in mass:
        if z == k:
            c += 1
        if c > res[1]:
            res[0] = z
            res[1] = c
if res[1] == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {res[0]} встретилось {res[1]} раз')
'''

t3 = '''
import random

SIZE_N = 1000
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
res = [0, 0]

for i in range(len(mass)):
    c = 0
    z = mass[i]
    for k in mass:
        if z == k:
            c += 1
        if c > res[1]:
            res[0] = z
            res[1] = c
if res[1] == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {res[0]} встретилось {res[1]} раз')
'''

# -------------------------------------------------------------------------------------------------
# Версия 2 - улучшенная

t4 = '''
import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = 0

for i in mass:
    a = mass.count(i)
    if z < a:
        z = a
        k = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {k} встретилось {z} раз')
'''

t5 = '''
import random

SIZE_N = 100
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = 0

for i in mass:
    a = mass.count(i)
    if z < a:
        z = a
        k = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {k} встретилось {z} раз')
'''

t6 = '''
import random

SIZE_N = 1000
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = 0

for i in mass:
    a = mass.count(i)
    if z < a:
        z = a
        k = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {k} встретилось {z} раз')
'''

# -------------------------------------------------------------------------------------------------
# Версия 3 - улучшенная  ?

t7 = '''
import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = [0, 0]

for i in mass:
    a = mass.count(i)
    if z[0] < a:
        z[1] = a
        z[0] = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {z[0]} встретилось {z[1]} раз')
'''

t8 = '''
import random

SIZE_N = 100
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = [0, 0]

for i in mass:
    a = mass.count(i)
    if z[0] < a:
        z[1] = a
        z[0] = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {z[0]} встретилось {z[1]} раз')
'''

t9 = '''
import random

SIZE_N = 1000
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

z = [0, 0]

for i in mass:
    a = mass.count(i)
    if z[0] < a:
        z[1] = a
        z[0] = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {z[0]} встретилось {z[1]} раз')

'''

# Версия 1 - оригиинальная
print(timeit.timeit(t1, number=10))  # для 10 значений при 10 измерениях в списке t = 0.004317399999999999
print(timeit.timeit(t2, number=10))  # для 100 значений при 10 измерениях в списке t = 0.016630500000000006
print(timeit.timeit(t3, number=10))  # для 1000 значений при 10 измерениях в списке t =  1.4740493000000001
cProfile.run(t1)
cProfile.run(t2)
cProfile.run(t3)


# Версия 2
print(timeit.timeit(t4, number=10))  # для 10 значений при 10 измерениях в списке t = 0.0038855
print(timeit.timeit(t5, number=10))  # для 100 значений при 10 измерениях в списке t = 0.00426979999999999
print(timeit.timeit(t6, number=10))  # для 1000 значений при 10 измерениях в списке t =  0.2458632
cProfile.run(t4)
cProfile.run(t5)
cProfile.run(t6)

# # Версия 3
print(timeit.timeit(t7, number=10))  # для 10 значений при 10 измерениях в списке t = 0.003467799999999993
print(timeit.timeit(t8, number=10))  # для 100 значений при 10 измерениях в списке t = 0.24707910000000002
print(timeit.timeit(t9, number=10))  # для 1000 значений при 10 измерениях в списке t =  0.24997429999999998
cProfile.run(t7)
cProfile.run(t8)
cProfile.run(t9)

'''

Библиотеки покаывают что версия 2, 3 примерно одинаковы. При количестве данных 1000 эллемнтов в списке 
версия 3  работает быстрее, но при увелечении до 50_000 версия 2 работает быстрее ~1 сек быстрее. 

'''