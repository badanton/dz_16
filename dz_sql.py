# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

import sqlite3
import random

# Создаём Базу данных
conn = sqlite3.connect('bd_sql.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER,col_2 INTEGER) ''')

# Заполняем таблицу данными
a = [random.randint(0, 9) for i in range(2)]

cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (a[0], a[1]))
# Сохраняем изменения
#conn.commit()

cursor.execute('''SELECT col_1, col_2  FROM tab_1''')
k = cursor.fetchall()
a = [j for i in k for j in i]
average = sum(a)/len(a)
quantity = len(k)
print('Содержание колонок :', k)
print('Среднее арифметическое : ', average)
print('Количество записей в бд :', quantity)


if average > quantity:
    cursor.execute('''DELETE FROM tab_1 WHERE id > 4''')
    conn.commit()
    k = cursor.fetchall()
    print('Содержание колонок после удаления :',k)
else:
    print(f'Среднее арифметическое всех элементов {average} меньше количества записей {quantity}')

cursor.execute('''SELECT id  FROM tab_1''')
m = cursor.fetchall()
print(m)