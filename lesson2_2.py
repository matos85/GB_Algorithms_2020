'''
https://app.diagrams.net/#G15Xt2S6YHrGTG3cB_mzBjEa676TkBC4-i

 Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

print('Введите натуральное число')
k = int(input('Ваше число: '))
z = 0.1
y = 0
x = 0
for i in range(1, len(str(k)) + 1):
    if len(str(i)) == len(str(k)):
        if (k == 2) or (k == 4) or (k == 6) or (k == 8) or (k == 0):
            y += 1
        else:
            x += 1
    else:
        z *= 10
    if ((k // z) % 2 == 0):
        y += 1
    else:
        x += 1

print(f'Нечетных: {x}, Четных: {y}')
