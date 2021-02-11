'''
 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
  Найдите в массиве медиану.

  Медианой называется элемент ряда,   делящий его на две равные части:
                в одной находятся элементы, которые не меньше медианы,
                в другой — не больше медианы.

Примечание:
задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
 который не рассматривался на уроках (сортировка слиянием также недопустима).

'''
import random
from collections import defaultdict

my_dict = defaultdict(list)

m = int(input('Введите  число для расчета длины массива: '))

SIZE_N = 2 * m + 1
MIN_ITEM = -1_000_000
MAX_ITEM = 1_000_000
mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]


print(mass)
print('*' * 10)
# автоматическая сортировка для самопроверки
print(f'Автоматическая сортировака \n{sorted(mass)} для  удобства проверки ответа')
print('*' * 10)
# Решение задачи 
print('Поиск медианы')
for i in mass:
    mini = 0
    maxi = 0
    if i <= -1:
        for z in range(len(mass)):
            if i < mass[z]:
                maxi -= 1
            if i > mass[z]:
                mini -= 1
        my_dict[i].append(maxi)
        my_dict[i].append(mini)
    if i > -1:
        for z in range(len(mass)):
            if i < mass[z]:
                maxi += 1
            if i > mass[z]:
                mini += 1
        my_dict[i].append(maxi)
        my_dict[i].append(mini)
for k, v in my_dict.items():
    for j in range(len(v)):
        if abs(v[j]) == m:
            between = k
    else:
        if len(v) / 2 > m:
            between = k
print(between)
