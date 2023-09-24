"""
Задача 30:  Заполните массив элементами арифметической 
прогрессии. Её первый элемент, разность и количество 
элементов нужно ввести с клавиатуры. Формула для получения 
n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

"""
first_el = int(input("Введите первый элемент арифметической прогрессии: "))
diff = int(input("Введите разность арифметической прогрессии: "))
amount = int(input("Введите количество элементов арифметической прогрессии: "))

progression = []

progression.append(first_el)
for i in range(amount):
    if i >= 2:
        progression.append(first_el + diff*(i-1))

for i in range(len(progression)):
    print(progression[i])
"""

"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. не 
меньше заданного минимума и не больше заданного максимума).

"""

import random

arr_length = int(input("Введите длинну сиписка: "))
min_am = int(input("Введите минимальное число диапазона поиска: "))
max_am = int(input("Введите максимальное число диапазона поиска: "))

arr = []
search = []

for i in range(arr_length):
    arr.append(random.randint(0,100))

print(arr)

for i in range(len(arr)):
    if arr[i] >= min_am and arr[i] <= max_am:
        search.append(i+1)

print(search)