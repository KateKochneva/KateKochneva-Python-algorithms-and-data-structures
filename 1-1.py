# https://drive.google.com/file/d/1lTmHywi3cLmdgoXFeCrc0yGm9HnPVbX3/view?usp=sharing

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
summa = d1 + d2 + d3
multiplication = d1 * d2 * d3
print("Сумма цифр числа:", summa)
print("Произведение цифр числа:", multiplication)