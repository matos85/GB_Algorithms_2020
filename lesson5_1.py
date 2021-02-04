'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
 для каждого предприятия. Программа должна определить среднюю
  прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, 
  чья прибыль выше среднего и ниже среднего.

'''

from collections import defaultdict

businesses = defaultdict(list)
Flag = True

print(
    'Введите количестов предприятий и их прибыль за 4ре квартала.\n'
    'Для завершения работы программы введите 0 - ноль.')
while Flag:
    num = input('Введите количество предприятий: ')
    if int(num) == 0:
        Flag = False
        break
    if num.isdigit() and int(num) > 0:
        num = int(num)
        for i in range(1, num + 1):
            name_businesses = input(f'Введите название {i}-го предприятия: ')
            profit = 0
            for i in range(1, 5):
                profit = int(input(f'Введите прибыль за {i}-й квартал: '))
                businesses[name_businesses].append(profit)
        else:
            Flag = False

print('-' * 50)
print(*businesses)

k = 0
sum_ = 0
for name, profits in businesses.items():
    p = 0
    for i in profits:
        p += i
    businesses[name] = p
    sum_ += p
    k += 1

print('-' * 50)
# print(f'Сумма: {sum_}, Количество: {k}')
avarages = sum_ / k
print(f'Средняя прибыль: {avarages}')

print('-' * 50)

print('Предприятия с прибылью выше средней: ')
for name, profits in businesses.items():
    if float(profits) > avarages:
        print(name)

print('Предприятия с прибылью ниже средней: ')
for name, profits in businesses.items():
    if float(profits) < avarages:
        print(name)
