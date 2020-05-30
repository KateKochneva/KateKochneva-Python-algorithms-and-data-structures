# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# # Примечание. Идеальным решением будет:
# # ● выбрать хорошую задачу, которую имеет смысл оценивать,
# # ● написать 3 варианта кода (один у вас уже есть),
# # ● проанализировать 3 варианта и выбрать оптимальный,
# # ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# # ● написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit
import cProfile

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

# 1 решение
def test_1(N):
    array_1 = [random.randint(0, 10) for _ in range(N)]
    #print(array_1)
    minimum_index = int()
    for t in range(1, 3):
        minimum = array_1[0]
        for i in range(1, len(array_1)):
            if array_1[i] < minimum:
                minimum = array_1[i]
                minimum_index = array_1.index(minimum)
        #print(minimum)
        array_1.remove(minimum)

print(timeit.timeit('test_1(10)', number=100, globals=globals())) # 0.0037863000000000063, N = 10
print(timeit.timeit('test_1(100)', number=1000, globals=globals())) # 0.29431260000000004, N = 100
print(timeit.timeit('test_1(1000)', number=1000, globals=globals())) # 2.968503, N = 1000

cProfile.run('test_1(10)')  #  11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_1(100)') # 137    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_1(1000)')# 1444   0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



#2 решение
def test_2(N):
    array_1 = [random.randint(0, 100) for _ in range(N)]
    if array_1[0] < array_1[1]:
        minimum_1 = 0
        minimum_2 = 1
    else:
        minimum_1 = 1
        minimum_2 = 0

    for i in range(2, len(array_1)):
        if array_1[i] < array_1[minimum_1]:
            t = minimum_1
            minimum_1 = i
            if array_1[t] < array_1[minimum_2]:
                minimum_2 = t
        elif array_1[i] < array_1[minimum_2]:
            minimum_2 = i

    #print(f'Число: {array_1[minimum_1]}')
    #print(f'Число: {array_1[minimum_2]}')

print(timeit.timeit('test_2(10)', number=100, globals=globals()))    # 0.0032565000000000094, N = 10
print(timeit.timeit('test_2(100)', number=1000, globals=globals()))   # 0.464253, N = 100
print(timeit.timeit('test_2(1000)', number=1000, globals=globals()))   # 3.339482, N = 1000

cProfile.run('test_2(10)')  # 13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_2(100)') # 116   0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_2(1000)')# 1264  0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



# 3 решение
def test_3(N):
    array_1 = [random.randint(0, 100) for _ in range(N)]
    minimum_1 = min(array_1)
    array_1.remove(minimum_1)
    minimum_2 = min(array_1)
    #print(f'Число: {minimum_1}')
    #print(f'Число: {minimum_2}')

print(timeit.timeit('test_3(10)', number=100, globals=globals()))    # 0.002946000000000004, N = 10
print(timeit.timeit('test_3(100)', number=1000, globals=globals()))   # 0.2595363, N = 100
print(timeit.timeit('test_3(1000)', number=1000, globals=globals()))   # 2.8892015, N = 1000

cProfile.run('test_3(10)') # 14     0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_3(100)') # 123   0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('test_3(1000)')# 1242  0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Вывод:
# Третий вариант самый быстрый потому что эти функции разработаны на языке С и, скомпилированы в машинный код
# и более быстро выполняются
# Первый и второй варианты похожи по времени, первый выполняется немного быстрее

