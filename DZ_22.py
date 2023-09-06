class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"\n{self.name}", "=>", end="")


class Computer(Student):
    def __init__(self, name, model, processor, ram):
        super().__init__(name)
        self.model = model
        self.processor = processor
        self.ram = ram

    def info(self):
        super().info()
        print(f" {self.model}, {self.processor}, {self.ram}", end="")


group = [
    Computer("Roman", "HP", "i7", 16), Computer("Vladimir", "HP", "i7", 16)
]
for i in group:
    i.info()
