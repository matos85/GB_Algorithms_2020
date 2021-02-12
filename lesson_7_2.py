'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
  Выведите на экран исходный и отсортированный массивы.

'''
import random

SIZE_N = 10
SIZE_M = 5
MIN_ITEM = 0
MAX_ITEM = 50
mass = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]

print(mass)


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list[:]
    middle = int(len(my_list) / 2)
    left = merge_sort(my_list[:middle])
    right = merge_sort(my_list[middle:])
    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


print(merge_sort(mass))