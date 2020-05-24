# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
# должна принимать на вход натуральное и возвращать соответствующее простое число.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import math
#1)
def sieve(nat):
    n = 100
    sieve = [i for i in range(n)]
    print(sieve)
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    #print(res)
    return res[nat-1]

for t in range(1, 20):
    p = sieve(t)  #нат число
    print(p)

#------------------
#2)
def prime(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

user_number = int(input('Введите номер по счету простого числа: '))
print(prime(user_number))


