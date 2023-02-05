num = 12345
a = num % 10
print("a =", a)
num = num // 10
b = num % 10
print("b =", b)
num = num // 10
c = num % 10
print("c =", c)
num = num // 10
d = num % 10
print("d =", d)
num = num // 10
e = num % 10
print("e =", e)
print(a, b, c, d, e)
print(a*10000+b*1000+c*100+d*10+e*1)
print("Произведение цифр равно:", a * b * c * d * e)
print("Среднее арифметическое цифр равно:", (a + b + c + d + e) // 5)
