# https://drive.google.com/file/d/1lTmHywi3cLmdgoXFeCrc0yGm9HnPVbX3/view?usp=sharing

# 8. Определить, является ли год, который ввел пользователь, високосным или не високосным

year = int(input())
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("usual year")
else:
    print("intercalary year")