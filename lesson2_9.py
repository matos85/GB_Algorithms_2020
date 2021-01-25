'''
https://drive.google.com/file/d/15Xt2S6YHrGTG3cB_mzBjEa676TkBC4-i/view?usp=sharing

Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.

'''


def amount(n):
    if n < 10:
        return n
    else:
        return amount(n // 10) + n % 10


x = 0
print('Вводите натуральные числа. Для выхода введите 0.')
# Если новое число будет по сумме цифр меньше предидущего то будет выведено преидущее так как оно больше
while True:
    n = int(input('Введите натуральное число: '))
    if n == 0:
        break
    else:
        n = amount(n)
        if x < n:
            x = n
            print(x)
        else:
            print(x)
