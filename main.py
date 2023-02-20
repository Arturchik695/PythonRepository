# name_1 = "Arthur"  # Если что-то подчеркивает, то Ctrl+Alt+L
# print("Hello,", name_1)
# age = 20
# print(age)

# a = 5
# print(a)
# print(type(a))
# b = "6"
# print(type(a))
# print(b)
# print(a * b)

# a = 4
# b = 5
# print(b)
# print(id(a))
# a = b
# print(a)
# print(id(a))

# a = b = c = 5
# a, b, c = 2, "Hello", 4.5
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# print("Документ \"file.py\" находится по заданному пути: \nD:\\python\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)

# print(3333333333333333333333333)
# print(3.333333333333333333333333)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 2)
# print(6 // 2)
# print(6 % 2)

# a = 5
# b = 7
# c = 3
# print("Сумма = ", + a + b + c)
# print("Произведение = ", + a * b * c)
# print("Среднее арифметическое = ", + (a + b + c) / 3)

# n = 1234
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# print(a, b, c, d)
# print(d, c, b, a)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # c=1
# # a = b  # a=2
# # b = c  # b=1
# print("a:", a)
# print("b:", b)

# Функции явного преобразования типов:
# int()
# str()
# float()

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# a = 3.891
# a = round(a, 2)
# print(a)
# print(type(a))
# bool()

# num1 = "2.6"
# num2 = 10
# c = float(num1) + num2
# print(c)

# name = "Виктор"
# age = 26
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" ")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print("Вас зовут", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# sum1 = a+b
# sum2 = c+d
# print("Сумма1 равна:", sum1)
# print("Сумма2 равна:", sum2)
# print("Результат деления:", round((sum1/sum2), 2))

# b1 = True
# b2 = False
# print(b1 + 5)  # True(1) + 5 = 6
# print(int(b1))
# print(b2 * 5)  # False(0) + 5 = 0
# print(int(b1))

# print(bool("Python"))
# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# print(7 == 7)
# print(2 + 5 == 9 - 2)
# print(7 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 <= 8)
# print("привет" > "Привет")

# True && True = True
# True && False = False

# and / or / not
# print(not 9 - 5)
# print(not 9 - 9)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен!")

# a = 25
# b = 15
# if a > b:
#     print("a>b")
# elif b > a:
#     print("b>a")
# else:
#     print("a==b")


# a = input("a: ")
# b = input("b: ")
# c = input("c: ")
# if a == b == c:
#     print("Равносторонний")
# elif a == b or b == c or c == a:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует!")


# month = int(input("Введите номер месяца: "))
# if 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# elif month == 12 or month == 1 or month == 2:
#     print("Зима")
# else:
#     print("Такого месяца не существует")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_3
#     case шаблон_n:
#         действие_n
#     case _:
#         действие по умолчанию


# password = "qwerty"
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print("Модератор")
#     case _:
#         print("Пароль не верен")


# day = "вторник"
# time = 14
# match day:
#     case "понедельник" | "вторник"| "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a==b" if a == b else "a>b" if a > b else "b>a")

# a, b = 10, 5
# print("На ноль делить нельзя" if b == 0 else "Результат:", a / b)


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так")
# else:
#     print("Все норм. Введены числа", n, "и", m)
# finally:
#     print("Конец программы")
# print("\nКод далее")


# a = input("Введите первое значение: ")
# b = input("Введите второе значение: ")
# try:
#     print(int(a)+int(b))
# except ValueError:
#     print(a+b)


# Циклы
# i = 5
# while i < 5:
#     print("i= ", i)
#     i += 1

# n = int(input("Укажите количество символов"))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     print(a, end=" ")
#     if a % 2:
#         res += a
#     a += 1
# print("\n", res)


# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n=int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue  # перебрасывает на проверку условия while, поэтому нет 3
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(end=" ")
#         j += 1
#     print("*")
#     i += 1


# for element in collection:
#     тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green':
#     print(color)

# a = int(input("Введите целое число: "))
# for i in range (1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done!")


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end=" ")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# w = [letter for letter in "Hello"]
# print(w)
# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# Списки

# nums = [8,3,9,4,1,[2,5,6]"H",2.6,True]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]  # 0,1,2,3,4 но в другую сторону -1,-2,-3,-4,-5
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))

# s = [5] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
#
# c = s + b
# print(c)


# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")


# Генератор списков

# a = [0 for i in range(5)]
# a[0] = 5
# print(a)
#
# a = [i for i in range(5)]
# print(a)
#
# n = 5
# a = [i ** 2 for i in range(5)]
# print(a)
#
# a = [i * 3 for i in "list"]
# print(a)

# 1ый способ
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# 2ой способ
# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)


# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":", a[i])
# print()
#
# for i in a:
#     print(i)

# # 1ый способ
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
#     print(s)
#
# # 2ой способ
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
#     print(s)


# n = list(range(21, 41))
# print(n)
# k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
# print("Количество нечетных элементов: ", k)
# s = 0
# for i in range(len(n)):
#     if n[i] % 2 != 0:
#         s += n[i]
# print("Сумма нечетных элементов: ", s)


# n = list(range(21, 41))
# print(n)
# k = 0
# s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество нечетных элементов: ", k, "\nСумма нечетных элементов: ", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# k = 0
# s = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#         s += a[i]
# print(s / k)

# a = [6, 3, 0, 8, 2]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез
# Список[star:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[:2])
# print(a[2:])
# print(a[4:1:-1])
# a = "Hello"
# print(a[1:3])

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:5]
# print(a)

# Методы списка
# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append(99)  # добавляет элемент в конец списка
# print(a)
# a.extend([5, 6, 7])
# a.extend("add")  # добавляет список элементов в конец списка
# print(a)

# a = []
# # a.extend([i**2 for i in range(1, 11)])
# # print(a)
# for i in range(1, 11):
#     a.extend([i**2])
# print(a)


# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)  # добавляет элемент в определенное место списка
# print(a)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "число не делиться на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a(i))
#     c.append(b(i))
# print(c)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(2)  # удаляет первый по найденному совпадению элемент из списка
# print(a)
# last = a.pop()  # удаляет последний элемент из списка (без параметров) и возвращает удаленный элемент
# print(a)
# second = a.pop(-2)  # удаление элемента по индексу
# print(a)
# print(second)
# a.clear()  # очищает список
# print(a)


# s = []
# n = int(input("Введите элементы списка: "))
# for i in range(n):
#     x = int(input("-> "))
#     s.append(x)
# k = int(input("Введите индекс: "))
# print("k = ", k)
# s.pop(k)
# print(s)

# Короткая запись
# s = [int(input("-> ")) for i in range (int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс:\nk = "))
# s.pop(k)
# print(s)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(2)  # считает кол-во заданных значений в списке
# print(num)
#
# ind = a.index(9)  # возвращает положение первого индекса по заданному значению
# print(ind)


# c = [1, 2, 3]
# d = c.copy()  # возвращает копию списка
# print("c = ", c)
# print("d = ", d)
# c.append(4)
# d.insert(0, 100)
# print("c = ", c)
# print("d = ", d)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.reverse()  # переворачивает список
# print(a)
#
# a.sort()  # отсортировывает элементы по возрастанию
# print(a)
#
# a.sort(reverse=True)  # по убыванию
# print(a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort()  # сортировка по алфавиту
# print(s)
#
# s.sort(key=len)  # сортировка по кол-ву букв
# print(s)
#
# a.sort(reverse=True)
# print(a)
#
# b = sorted(a, reverse=True)
# print("b = ", b)
# print("a = ", a)


# Генерация случайных данных

# import random as r
# print(r.random())
# print(r.randint(0, 5))
# print(r.randrange(6, 15, 2))

# from random import randint, randrange
# print(randint(0, 5))
# print(randrange(6, 15, 2))


# from random import *
#
# print(random())
# print(randint(0, 5))
# print(randrange(6, 15, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# # city_list = ['Москва', 'Воронеж', 'Сочи', 'Екб', 'Спб']
# city_list = 'Воронеж'
# print(choice(city_list))
# print(choices(city_list, k=3))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))


# from random import randint
#
# mas = [randint(0, 20) for i in range(10)]
# print(mas)

# lst = [7, 12, 20, 28, 9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))


# from random import randint
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)


# from random import randint
#
# mas = [randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)


# from random import randint
#
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# min_1 = min(lst)
# print(min_1)
# ind = lst.index(min_1)
# del lst[:ind]
# print(lst)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("!!!!Список пустой")


# from random import randint
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
#
# print("Первый список: ", a)
# print("Второй список: ", b)
#
# # с = a + b
# # print("Третий список:  ")
#
# # c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# # print("Элементы обоих списков: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# from random import randint
# k = int(input("Введите размер списка: "))
# s = []
# while len(s) < k:
#     w = randint(0, k-1)
#     if w not in s:
#         s.append(w)
# print(s)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # print(len(m))
# print(m)
# # print(m[1][2])
#
# # a = [2, 'hello', 5]
# # print(a[1][1])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x**2, end="\t\t")
#     print()


# matrix = [[x * y for x in range(1, 10)] for y in range(1, 10)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# matrix = []
# for y in range(3):
#     new_row = []
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# print("Проверка репозитория")
# print("Клон")


# 1 способ импорта
# import math
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# 2 способ импорта
# from math import sqrt, floor
# num1 = sqrt(4)
# num2 = floor(3.2)

# 3 способ импорта
import math as m
import time

# from math import pi
# r = int(input("Введите радиус окружности: "))
# s = round(2 * pi * r, 2)
# print(s)


# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# s = time.time()
# print(s)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня %B, %d (%A), %Y"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print("Программа завершена")

# text = input("Название упоминания: ")
# t = float(input("Через сколько минут: "))
# t = t * 60
# time.sleep(t)
# print(text)


# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello,", name)
#
#
# hello("Arthur")

# def get_sum(a, b):
#     print("Сумма: ")
#     return a + b  # ниже return ничего не пишем
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# # get_sum("2", "5")
# print(res)  # ничего не вернулось


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#     # def symbol(count, a, b):
#     #     for i in range(count):
#     #         x = a if i % 2 else b
#     #         print(x, end="")
#     #     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def res(a, b):
#     if a > b:
#         print(a - b)
#     else:
#         print(a + b)
#
#
# x = int(input("->"))
# y = int(input("->"))
# res(x, y)


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе: =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a=0, b=0, c=20, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# e = 2
# print(get_sum(1, 5, d=e))
# print(get_sum())
# print(get_sum(d=1, a=5))
# print("Результат", get_sum(2, d=1, c=5), end="\n\n", sep="!!!")
# print(get_sum(1, 5, d=e))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


# def summa(a, b, c):
#     sm = a + b + c
#     avg = sm / 3
#     return avg
#
#
# q = summa(1, 2, 3)
# print(q)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def add_number(n):
#     print("n:", n, "=", id(n))
#     n += 1
#     print("n:", n, "=", id(n))
#     return n
#
#
# x = 1
# print("x:", x, "=", id(x))
# y = add_number(x)
# print("x:", x, "=", id(x))
# print("y:", y, "=", id(y))


# def add_number(n):
#     print("n:", n, "=", id(n))
#     n = n + [4]  # n += [4]
#     print("n:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print("x:", x, "=", id(x))
# add_number(x)
# print("x:", x, "=", id(x))


# Кортеж (tuple)

# a = 1,
# print(a)
# print(type(a))
# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(type(b))

# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])
# # tpl[2] = 10
# print(tpl[1:3])

# s = tuple(input("->") for i in range(3))

# from random import randint
# s = tuple(randint(1, 30) for i in range(10))
# print(s)

# s = tuple(2 ** i for i in range(1, 12))
# print(s)

# t1 = tuple("hello")
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(t3 * 2)
# print(len(t3))
# print(t3.count('l'))  # ищет количество букв l
# print(t3.index('l'))  # ищет первое вхождение l

# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")


# t1 = tuple("hello")
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# for i in t3:
#     print(i, end="")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def tpl(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = tpl(0, 5)
# tpl2 = tpl(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print(tpl3.count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst = list(tpl)
# print(type(lst))
# print(lst)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "\nНаселение:", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, " (Население: ", city_population, ")", sep="")


# Множество (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))
# lst = ["banana", "apple", "orange", "banana", "apple"]
# a = set(lst)
# a = set("Hello")
# print(type(a))
# print(a)


# def to_set(a):
#     x = set(a)
#     n = len(x)
#     return x, n
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# print("green1" not in t)
# for i in t:
#     print(i)


# lst = {'ab_1', 'ac_2', 'bc_1', 'bc_2'}
# a = {i for i in lst if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'}
# print(a)

# Альтернативная запись:
# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# users = {"Tom", "Alice", "Bob"}
# users.add("Ann")
# print(users)
# user = "Tom"
# if user in users:
#     users.remove(user)
# print(users)
# users.discard("Rob")
# print(users)
# users.pop()
# print(users)
# users.clear()
# print(users)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# c = a & b
# c = a ^ b
# c = a |= b
# c = a &= b
# print(c)
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# a = set(input("Введите первую строчку: "))
# b = set(input("Введите вторую строчку: "))
# c = a & b
# print(c)


# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one = drawing ^ music
# print(one)
#
# both = drawing & music
# print(both)
#
# drawing = drawing - both
# print(drawing)


# frozenset (замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset("hello")
# print(a)


# Словарь (dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])


# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)


# d = {"one": 1, "two": 2, "three": 3}
# print(list(d))
# lst = ["one", "two", "three"]
# # print(dict(lst))
#
# a = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
# print(dict(a))


# d = {"one": 45, 0: "text", (1, 2.3): 'Кортеж', 43: [2, 3, 6, 7], 0: "text111", 1: "text"}
# print(d)  # значения словаря ТОЛЬКО из неизменяемых типов данных
# # в ключах с одинаковыми названиями значения перезаписываются
# # ключи должны быть уникальными!
# print(d[0][1])  # обращение к ключу


# d = {i: i ** 2 for i in range(2, 7)}
# d = {i: input("->") for i in range(2, 7)}
# from random import randint
# d = {str(i) + "-й элемент": randint(1, 100) for i in range(1, 11)}
# print(d)


# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d['two'] = 200
# d['one'] += 100
# print(d)

# for key in d:
#     print(key, ":", d[key])











