import math


class Number:

    @staticmethod
    def max_number(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_number(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def sr_ar(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(x):
        for i in range(1, x):
            x = x * i
        return x


print(f"Максимальное число: {Number.max_number(3, 5, 7, 9)}")
print(f"Минимальное число: {Number.min_number(3, 5, 7, 9)}")
print(f"Среднее арифметическое: {Number.sr_ar(3, 5, 7, 9)}")
print(f"Факториал числа: {Number.factorial(5)}")


