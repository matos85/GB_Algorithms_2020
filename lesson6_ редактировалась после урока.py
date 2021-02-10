'''
Пункт 1:
Задача из урока 3 номер задачи 4:
Определить, какое число в массиве встречается чаще всего.

Пункт 2:
Три варианта решения задачи см. ниже

Пункт 3:
см ниже			# эта часть добавлена после  урока

Пункт 4:
Вариант 2 являетя оптимальным для данной задачи по потреблению памяти.
Win10 x64 - Python 3.8
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32	# эта часть добавлена после  урока

Пункт 5:
	------ Результаты варианта 1 ------
type(obj)=<class 'list'>	sys.getsizeof(obj)=4508
type(obj)=<class 'list'>	sys.getsizeof(obj)=36


		------ Результаты варианта 2 ------
type(obj)=<class 'tuple'>	sys.getsizeof(obj)=4020
type(obj)=<class 'int'>	sys.getsizeof(obj)=14	5


		------ Результаты варианта 3 ------
type(obj)=<class 'collections.deque'>	sys.getsizeof(obj)=4272
type(obj)=<class 'collections.defaultdict'>	sys.getsizeof(obj)=10300


'''
import collections
import sys
import random
from collections import deque

sum_list = []   # эта часть добавлена после  урока


def show(obj):
    x = sys.getsizeof(obj)  # эта часть добавлена после  урока
    sum_list.append(x)  # эта часть добавлена после  урока
    print(f'{type(obj)=}\t{sys.getsizeof(obj)=}\t{obj}')
    # Этот участок кода закоментирован для краткости вывода
    # if hasattr(obj, '__iter__'):
    #     if hasattr(obj, 'items'):
    #         for key, value in obj.items():
    #             print('\n')
    #             show(key)
    #             show(value)



SIZE_N = 1_0
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 1000

# Версия 1 - оригинальная

mass1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
list1 = [0, 0]
my_variables_1 = []

for i in range(len(mass1)):
    c = 0
    z1 = mass1[i]
    for k in mass1:
        if z1 == k:
            c += 1
        if c > list1[1]:
            list1[0] = z1
            list1[1] = c

if list1[1] == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {list1[0]} встретилось {list1[1]} раз')

# -----------------------------------------------------------------------
# Версия 2 - улучшенная

mass2 = tuple([random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)])
z = 0
k = None
for i in mass2:
    a = mass2.count(i)
    if z < a:
        z = a
        k = i
if z == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    print(f'Число {k} встретилось {z} раз')

# -----------------------------------------------------------------------
# Версия 3 - улучшенная

mass3 = deque([random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)])
list3 = collections.defaultdict(list)

for i in mass2:
    a = mass3.count(i)
    list3[i].append(a)
sorted(list3)

if list3.values() == 1:
    print('Все числа в списке встречаются по 1 разу')
else:
    for k, v in list3.items():
        print(f'Число {k} встретилось {v[0]} раз')
        break

# ---------------------------------------------------------------------
# Вызов функции для вывода памяти
my_variables = [mass1, list1, mass2, z, mass3, list3]
u = 0
n = 1
for i in my_variables:
    if u == 0 or u == 2 or u == 4:
        print('\n')
        print(f'\t\t------ Результаты варианта {n} ------ ', end='\n')
        n -= 1
    show(i)
    u += 1
    n += 1


print(sum_list)             # эта часть добавлена после  урока
print(sum(sum_list))        # эта часть добавлена после  урока
