'''
Написать программу сложения и умножения двух  шестнадцатеричных чисел.При этом каждое число
представляется как коллекция, элементы которой — цифры числа.Например, пользователь
ввёл A2 и C4F. Нужно  сохранить их как[‘A’, ‘2’] и[‘C’, ‘4’, ‘F’] соответственно.Сумма
чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

'''

from collections import deque


def sum_hex(x, y):
    HEX_deque = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    shift = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = HEX_deque[x.pop()] + HEX_deque[y.pop()] + shift

        else:
            res = HEX_deque[x.pop()] + shift

        shift = 0

        if res < 16:
            result.appendleft(HEX_deque[res])

        else:
            result.appendleft(HEX_deque[res - 16])
            shift = 1

    if shift:
        result.appendleft('1')

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print('Ответ: ', *sum_hex(a, b))
