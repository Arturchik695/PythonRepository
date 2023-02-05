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

print("Проверка репозитория")




