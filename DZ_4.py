from random import randint
mas = [randint(1, 100) for i in range(1)]
n = int(input("Введите число от 1 до 100: "))
if n == mas:
    print("Вы угадали!")
else:
    if n > max(mas):
        print("Загаданное число меньше")
        n = int(input("Введите число от 1 до 100: "))
    else:
        print("Загаданное число больше")
        n = int(input("Введите число от 1 до 100: "))


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# if a[i] % 2 == 0:
#     print(a[i])
