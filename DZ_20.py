class Car:

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.data}\nПроизводитель: {self.manufacturer}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.cost}")
        print("=" * 40)

    def __init__(self, model, data, manufacturer, power, color, cost):
        self.model = model
        self.data = data
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.cost = cost

    def set_model(self, model):  # установить
        self.model = model

    def get_model(self):  # получить
        return self.model

    def set_data(self, data):
        if isinstance(data, int):
            self.data = str(data) + " г."
        else:
            print("!!!Год выпуска должен быть числом!!!")

    def get_data(self):
        return self.data

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, power):
        if isinstance(power, int):
            self.power = str(power) + " л.с."
        else:
            print("!!!Мощность двигателя должна быть числом!!!")

    def get_power(self):
        return self.power

    def set_color(self, color):
        if isinstance(color, str):
            self.color = color
        else:
            print("!!!Цвет должен быть строкой!!!")

    def get_color(self):
        return self.color

    def set_cost(self, cost):
        if isinstance(cost, int):
            self.cost = str(cost) + " руб."
        else:
            print("!!!Цена должна быть числом!!!")

    def get_cost(self):
        return self.cost


h1 = Car('???', '???', '???', '???', '???', '???')
h1.set_model("X7 M50i")
h1.set_data(2021)
h1.set_manufacturer("BMW")
h1.set_power(530)
h1.set_color("Белый")
h1.set_cost(1000000)
h1.print_info()


