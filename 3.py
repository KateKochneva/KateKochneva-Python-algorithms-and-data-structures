import random
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 10_000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_2 = []
for i in array_1:
    if i%2 == 0:
        array_2.append(array_1.index(i))
print(array_1)
print(array_2)

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

maximum = array_1[0]
minimum = array_1[0]
for i in range(1, len(array_1)):
    if array_1[i] > maximum:
        maximum = array_1[i]
        maximum_index = array_1.index(maximum)
    elif array_1[i] < minimum:
        minimum = array_1[i]
        minimum_index = array_1.index(minimum)
if array_1.index(minimum)==0:
    minimum_index = 0
if array_1.index(maximum)==0:
    maximum_index = 0

array_1[maximum_index], array_1[minimum_index] = array_1[minimum_index], array_1[maximum_index]

print(array_1)
print(maximum)
print(minimum)
print(maximum_index)
print(minimum_index)

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

minimum_index = -1
for i in range(1, len(array_1)):
    if array_1[i] < 0 and minimum_index == -1:
        minimum_index = i
    elif array_1[i] < 0 and array_1[i] > array_1[minimum_index]:
        minimum_index = i
        i += 1
print(f" Число: {array_1[minimum_index]}, его индекс {minimum_index}.")


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

maximum = array_1[0]
minimum = array_1[0]
for i in range(1, len(array_1)):
    if array_1[i] > maximum:
        maximum = array_1[i]
        maximum_index = array_1.index(maximum)
    elif array_1[i] < minimum:
        minimum = array_1[i]
        minimum_index = array_1.index(minimum)
if array_1.index(minimum)==0:
    minimum_index = 0
if array_1.index(maximum)==0:
    maximum_index = 0

res = 0
flag = 0

if maximum_index > minimum_index:
    flag = 1
else:
    flag = 0

if flag == 1:
    for t in array_1[minimum_index:maximum_index+1]:
        res += t
else:
    for t in array_1[maximum_index:minimum_index]:
        res += t
print(res)

print(maximum)
print(minimum)
print(maximum_index)
print(minimum_index)

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)
minimum_index = int()
for t in range(1, 3):
    minimum = array_1[0]
    for i in range(1, len(array_1)):
        if array_1[i] < minimum:
            minimum = array_1[i]
            minimum_index = array_1.index(minimum)
    print(minimum)
    array_1.pop(minimum_index)
