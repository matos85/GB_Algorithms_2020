'''
 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
  заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
 Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

'''

import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = -100
MAX_ITEM = 100
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

print(mass)


def func(my_list):
    for e in range(len(my_list)):
        for i in range(len(my_list) - 1):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)
    return my_list

print('*' * 10)
print(func(mass))
