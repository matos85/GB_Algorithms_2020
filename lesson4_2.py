import timeit
import cProfile
# Вариант 1:
print('#Вариант 1:')
print('Нахождение просто числа. От 1 до 10_000 числа.')
num = int(input("Введите какое по счёту простое число вы хотите найти: "))


def my_sieve(num):
    def sieve(n):
        a = [0] * n
        for i in range(n):
            a[i] = i
        a[1] = 0
        m = 2
        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        del a
        return b

    lts = sieve(104750)
    return lts[num]


print(f'Ответ: {my_sieve(num - 1)}')

print('----------------------------------------------------------')

# Вариант 2:
print('#Вариант 2:')
print('Нахождение просто числа. От 1 до 10_000 числа.')
num = int(input("Введите какое по счёту простое число вы хотите найти: "))


def my_prime(num):
    a = [0]
    for k in range(2, 104750):
        n = k
        i = 2
        j = 0
        while i ** 2 <= n and j != 1:
            if n % i == 0:
                j = 1
            i += 1
        if j != 1:
            a.append(n)
    return a[num]


print(f'Ответ: {my_prime(num)}')

s1 = '''
num = 1000

def my_sieve(num):
    def sieve(n):
        a = [0] * n
        for i in range(n):
            a[i] = i
        a[1] = 0
        m = 2
        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        del a
        return b

    lts = sieve(104750)
    return lts[num]

#print(f'Ответ: {my_sieve(num - 1)}')
'''

s2 = '''
num = 1000

def my_prime(num):
    a = [0]
    for k in range(2, 104750):
        n = k
        i = 2
        j = 0
        while i ** 2 <= n and j != 1:
            if n % i == 0:
                j = 1
            i += 1
        if j != 1:
            a.append(n)
    return a[num]

#print(f'Ответ: {my_prime(num)}')
'''
print('----------------------------------------------------------')
print('Время выполнения:')
print(f'Вариант 1: {timeit.timeit(s1, number=3)}')
print(f'Вариант 2: {timeit.timeit(s2, number=3)}')
print('----------------------------------------------------------')
cProfile.run(s1)
cProfile.run(s2)


'''

#Вариант 1:
Нахождение просто числа. От 1 до 10_000 числа.
Введите какое по счёту простое число вы хотите найти: 10000
Ответ: 104729
----------------------------------------------------------
#Вариант 2:
Нахождение просто числа. От 1 до 10_000 числа.
Введите какое по счёту простое число вы хотите найти: 10000
Ответ: 104729
----------------------------------------------------------
Время выполнения:
Вариант 1: 2.8000000007466497e-06
Вариант 2: 7.000000010748408e-07
----------------------------------------------------------
         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Вариант 1 лучше так быстрее в 3.999999994924695 раза. Вариант 1 меет сложность  O(n log log n) 
'''