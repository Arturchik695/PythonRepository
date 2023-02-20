# Задача №1
d = {i: i**3 for i in range(1, 11)}
print(d)

# Задача №2
a = set(input("Введите первую строчку: "))
b = set(input("Введите вторую строчку: "))
a.difference_update(b)
print(a)

# Задача №3
a = set(input("Введите первую строчку: "))
b = set(input("Введите вторую строчку: "))
c = a.union(b)
print(c)

# Задача №4
a = set(input("Введите первую строчку: "))
b = set(input("Введите вторую строчку: "))
c = a.symmetric_difference(b)
print(c)




