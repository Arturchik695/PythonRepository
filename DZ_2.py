a = int(input("Введите число от 1 до 99: "))
k = a
if 1 <= a <= 99:
    if 11 <= a <= 14:
        print(a, "копеек")
    else:
        k = k % 10
        print(a, end=" ")
        if k == 1:
            print("копейка")
        elif 2 <= k <= 4:
            print("копейки")
        else:
            print("копеек")
else:
    print("Некорректное число")




