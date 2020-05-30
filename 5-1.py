#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque

b = deque()
d = dict()
NumberOfCompanies = int(input('Введите число предприятий: '))

for i in range(1, NumberOfCompanies + 1):
    Name = input('Введите наименование предприятия: ')
    lst = []
    a = deque()
    for p in range(1, 5):
        income = int(input(f'Введите прибыль за {p} квартал: '))
        lst.append(income)
    a.append(Name)
    a.append(sum(lst))
    b.append(a)

for i in b:
    name = i[0]
    d[name] = i[1]

average = sum(d.values())/NumberOfCompanies

print(f' Средняя прибыль предприятий за год: {average}')

for k in d.keys():
    if d[k] > average:
        print(f' Предприятие {k} имеет прибыль выше средней')
    elif d[k] < average:
        print(f' Предприятие {k} имеет прибыль ниже средней')
















