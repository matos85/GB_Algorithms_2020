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

Результаты:
Весрия 1 - оригинальная
Для 10 значений при 10 измерениях в списке t = 0.002769499999999994

         56 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



Для 100 значений при 10 измерениях в списке t = 0.0074113000000000095

         507 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.002    0.002 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      101    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Для 1000 значений при 10 измерениях в списке t = 0.7992283

         5023 function calls in 0.168 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.166    0.166    0.168    0.168 <string>:2(<module>)
        1    0.000    0.000    0.002    0.002 <string>:7(<listcomp>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1017    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

-------------------------------------------------------------------------------------------------

# Версия 2

Для 10 значений при 10 измерениях в списке t = 0.0001925999999998762


         65 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
       10    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Для 100 значений при 10 измерениях в списке t = 0.0027094999999999203

         610 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
      100    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      105    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Для 1000 значений при 10 измерениях в списке t = 0.18474039999999992

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.026    0.026 <string>:2(<module>)
        1    0.000    0.000    0.002    0.002 <string>:7(<listcomp>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     1000    0.024    0.000    0.024    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1023    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Версия 3

Для 1000 значений при 10 измерениях в списке t = 0.00036079999999993895

         65 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
       10    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Для 1000 значений при 10 измерениях в списке t = 0.004799599999999904

       607 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:200(randrange)
      100    0.000    0.000    0.000    0.000 random.py:244(randint)
      100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
      100    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

Для 1000 значений при 10 измерениях в списке t = 0.17731300000000005

         6032 function calls in 0.018 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.018    0.018 <string>:2(<module>)
        1    0.000    0.000    0.002    0.002 <string>:7(<listcomp>)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
     1000    0.016    0.000    0.016    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1027    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



Считаю что версия 2 быстрее.
Библиотеки покаывают что версия 2, 3 примерно одинаковы. При количестве данных 1000 эллемнтов в списке 
версия 3  работает быстрее, но при увелечении до 50_000 версия 2 работает быстрее ~1 сек.
 У всех вариантов сложность O(n) – линейная сложность



'''
