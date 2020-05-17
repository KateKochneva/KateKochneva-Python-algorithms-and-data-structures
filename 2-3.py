# https://drive.google.com/file/d/1i1yOx6okJy8e35rFcbbt_uxpMNekFKwz/view?usp=sharing
# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input())
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print(s)