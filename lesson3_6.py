'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и
 максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

'''

# import random
#
# SIZE_N = 10
# SIZE_M = 5
# MIN_ITEM = 0
# MAX_ITEM = 1000
# mass = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
mass = [8, 3, 2, 7, 8, 3,  9, 8, 8, 7, 7, 5, 8, 7, 6, 3, 8, 3,]
print(mass)
res = 0

minimum = mass[0]
maksim = mass[0]
for i, x in enumerate(mass, 1):
    if x < minimum:
        minimum = x
    if x > maksim:
        maksim = x

print(minimum)
print(maksim)

print('----------')

for i in mass:
    if i != minimum:
        if i != maksim:
            res += i

print(res)
