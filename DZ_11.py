# Задача №1
a = ['red', 'green', 'blue']
b = ['#FF0000', '#008000', '#0000FF']
d = dict(zip(a, b))
print(d)


# Задача №2
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
#
# # z = {}
# # z.update(a)
# # z.update(b)
# # z.update(c)
# z = a | b | c
# print(z)


# Задача №3
# workers = {
#     "emp1": {"name": "John", "salary": 7500},
#     "emp2": {"name": "Emma", "salary": 8000},
#     "emp3": {"name": "Brad", "salary": 6500}
# }
# for x in workers:
#     print(x)
#     for y in workers[x]:
#         print("\t", y, ": ", workers[x][y], sep="")
#
# key = input("Введите ключ работника: ")
# salary = input("Для изменения зарплаты введите - salary: ")
# print(workers[key][salary])
# new_data = int(input("Укажите новую зарплату: "))
# workers[key][salary] = new_data
# print(workers[key])


