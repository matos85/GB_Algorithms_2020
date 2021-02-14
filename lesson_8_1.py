''' Определение количества различных подстрок с использованием хеш-функции.
 Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''

import hashlib

s = input('Введите строку: ').lower()

substring = set()

for i in range(len(s)):
    for j in range(len(s), i, -1):
        hash_str = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
        substring.add(hash_str)

print(f'{len(substring) - 1} различных подстрок в строке {s}')
