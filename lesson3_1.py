'''
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

'''

my_list = [i for i in range(2, 100)]
d_range = [i for i in range(2, 10)]
res = {}

print(my_list)
print(d_range)
print('------ ' * 8)

for i in d_range:
    k = 0
    for z in my_list:
        if z % i == 0:
            k += 1
        res[i] = k

print(res)
