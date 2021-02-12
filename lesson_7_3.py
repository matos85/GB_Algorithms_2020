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
print(f'Длина массива: {len(mass)}')

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
        my_dict[i].append(abs(maxi))
        my_dict[i].append(abs(mini))
    if i > -1:
        for z in range(len(mass)):
            if i < mass[z]:
                maxi += 1
            if i > mass[z]:
                mini += 1
        my_dict[i].append(abs(maxi))
        my_dict[i].append(abs(mini))

num = 0
for k, v in my_dict.items():
    for j in range(len(v)):
#         if abs(v[j]) == m:
            a = k
        else:
            if v[j] / 2 > m:
                a = k
     # else:
    #     n = len(v)
    #     if num < n:
    #         num = n
    #         ln = v
    #         a = k

print(a)

#Вариант 2: Честно скажу с ним мне подсказали
# 
# 
# def heapify(nums, m_size, m_index):
#     # Индекс наибольшего элемента считаем корневым индексом
#     i_larg = m_index
#     left_child = (2 * m_index) + 1
#     right_child = (2 * m_index) + 2
# 
#     if left_child < m_size and nums[left_child] > nums[i_larg]:
#         i_larg = left_child
# 
#     # То же самое для правого потомка корня
#     if right_child < m_size and nums[right_child] > nums[i_larg]:
#         i_larg = right_child
# 
#     # Если наибольший элемент больше не корневой, они меняются местами
#     if i_larg != m_index:
#         nums[m_index], nums[i_larg] = nums[i_larg], nums[m_index]
#         heapify(nums, m_size, i_larg)
# 
# 
# def heap_sort(nums):
#     n = len(nums)
#     for i in range(n, -1, -1):
#         heapify(nums, n, i)
# 
#     for i in range(n - 1, 0, -1):
#         nums[i], nums[0] = nums[0], nums[i]
#         heapify(nums, i, 0)
# 
# 
# heap_sort(mass)
# 
# n = len(mass)
# if n % 2 == 0:
#     median1 = mass[n // 2]
#     median2 = mass[n // 2 - 1]
#     median = (median1 + median2) / 2
# else:
#     median = mass[n // 2]
# 
# print("Медиана: " + str(median))

