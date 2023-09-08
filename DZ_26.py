class Integer:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(f"Сторона должна быть целым положительным числом")
        instance.__dict__[self.name] = value


class Rectangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print(f"Треугольник со сторонами", (self.a, self.b, self.c), "существует")
        else:
            print(f"Треугольник со сторонами", (self.a, self.b, self.c), "НЕ существует")


r1 = Rectangle(2, 5, 6)
r2 = Rectangle(5, 2, 8)
r3 = Rectangle(7, 3, 6)
print(r1.__dict__)
r1.info()
r2.info()
r3.info()

