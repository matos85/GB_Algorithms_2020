'''
https://drive.google.com/file/d/1CyjAuUME30JNKKWAO-QjsAFzzZJ4auEE/view?usp=sharing


Задача №1
ПНайти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

print('Введите трехзначное число')
x = int(input('Ваше трехзначное число: '))
y = x % 10
z = x // 10
k = z % 10
c = z // 10
x1 = y + k + c
x2 = y * k * c
print(f'Cумма цифр из числа {x} равна: {x1}')
print(f'Произведение цифр из числа {x} равна: {x2}')
