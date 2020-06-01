# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# 3 урок 3 задание
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import sys
import random
#--------------------------------------------
def my_show(object):
    size = int()
    #print(f'type={type(object)}, size={sys.getsizeof(object)}, object={object}')
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                my_show(key)
                my_show(value)
        elif not isinstance(object, str):
            for item in object:
                #my_show(item)
                size += sys.getsizeof(item)
            return size
#1 решение
array_1 = [random.randint(0, 100) for _ in range(100)]

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

# print(array_1)
# print(maximum)
# print(minimum)
# print(maximum_index)
# print(minimum_index)

lst1 = []
lst1.append(sys.getsizeof(maximum))
lst1.append(sys.getsizeof(minimum))
lst1.append(sys.getsizeof(i))

summa_get = sum(lst1)
#print(summa_get)
summa_my_show = my_show(array_1)
#print(summa_my_show)
total_amount = summa_get + summa_my_show
print(total_amount)     # сумма 2872

#2 решение

array_2 = [random.randint(0, 100) for _ in range(100)]

minimum_index = 0
maximum_index = 0
for i in range(len(array_2)):
    if array_2[i] < array_2[minimum_index]:
        minimum_index = i
    elif array_2[i] > array_2[maximum_index]:
        maximum_index = i

array_2[minimum_index], array_2[maximum_index] = array_2[maximum_index], array_2[minimum_index]
#print(array_2)

lst2 = []
lst2.append(sys.getsizeof(maximum))
lst2.append(sys.getsizeof(minimum))
lst2.append(sys.getsizeof(i))

summa_get2 = sum(lst1)
#print(summa_get2)
summa_my_show2 = my_show(array_2)
#print(summa_my_show2)
total_amount2 = summa_get2 + summa_my_show2
print(total_amount2)     # сумма 2880



#3 решение

array_3 = [random.randint(0, 100) for _ in range(100)]
minimum = min(array_3)
maximum = max(array_3)
minimum_index = array_3.index(minimum)
maximum_index = array_3.index(maximum)
array_3[minimum_index], array_3[maximum_index] = array_3[maximum_index], array_3[minimum_index]
#print(array_3)

lst3 = []
lst3.append(sys.getsizeof(maximum))
lst3.append(sys.getsizeof(minimum))
lst3.append(sys.getsizeof(i))

summa_get3 = sum(lst3)
#print(summa_get3)
summa_my_show3 = my_show(array_3)
#print(summa_my_show3)
total_amount3 = summa_get3 + summa_my_show3
print(total_amount3)     # сумма 2876

# Вывод: у всех все 3 вариантах быстродействие переменных почти одинаковое. В итоге 1 место у 1 варианта,
# 2 место у 3 варианта и последнее - у второго.