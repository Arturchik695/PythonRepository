class Clock:
    __DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __eq__(self, other):
        return self.sec == other.sec

    def __lt__(self, other):
        return self.sec < other.sec

    def __gt__(self, other):
        return self.sec > other.sec


c1 = Clock(400)
c2 = Clock(200)
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")

if c1 < c2:
    print("Первый операнд меньше второго")
else:
    print("Второй операнд меньше второго")

if c1 > c2:
    print("Первый операнд больше второго")
else:
    print("Второй операнд больше первого")

c3 = c1 + c2
print(c1.get_format_time())
print(c2.get_format_time())
c2 += c1
print(c2.get_format_time())
print(c3.get_format_time())
c4 = c2 - c1
print(c4.get_format_time())
c2 -= c1
print(c2.get_format_time())
c5 = c2 * c1
print(c5.get_format_time())
c2 *= c1
print(c2.get_format_time())
c6 = c2 // c1
print(c6.get_format_time())
c2 //= c1
print(c2.get_format_time())
