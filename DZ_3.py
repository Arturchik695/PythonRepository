n = int(input("Укажите кол-во символов: "))
m = input("Укажите символ: ")
z = int(input("Укажите ориентацию линии:\n0 - горизонтальная \n1 - вертикальная\n"))
i = 0
while i < n:
    if z == 1:
        print(m)
    else:
        print(m, end="")
    i += 1
