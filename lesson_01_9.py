'''
https://drive.google.com/file/d/1CyjAuUME30JNKKWAO-QjsAFzzZJ4auEE/view?usp=sharing

Задача №9
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

print('Введите три разных числа')

x = int(input('Введите данные  первое целое число: '))
y = int(input('Введите данные  второе целое число: '))
z = int(input('Введите данные  третье целое число: '))

if x < z:
    if y < x:
        print(f'Среднее число среди введеных будет число: {x}')
    else:
        if y < z:
            print(f'Среднее число среди введеных будет число: {y}')
        else:
            print(f'Среднее число среди введеных будет число: {z}')
else:
    if x < y:
        print(f'Среднее число среди введеных будет число: {x}')
    else:
        if y < z:
            print(f'Среднее число среди введеных будет число: {z}')
        else:
            print(f'Среднее число среди введеных будет число: {y}')
