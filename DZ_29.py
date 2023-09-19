import sqlite3

cars = [
    ('BMW', 54000),
    ('Chevrolet', 46000),
    ('Daewoo', 38000),
    ('Citroen', 29000),
    ('Honda', 33000),
]

with sqlite3.connect("cars.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

    cur.executescript("""
    DELETE FROM cars WHERE model LIKE 'B%';
    UPDATE cars SET price = price + 100;
    """)  # Мультизапрос

cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})  # Изменение данных в таблице

cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)  # Заполнение данных из списка не в цикле

for car in cars:
    cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)  # Для заполнения данных в цикле из списка

# Единоразовый запрос:
cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
cur.execute("INSERT INTO cars VALUES(5, 'Audy', 52000)")
