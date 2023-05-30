# 1.Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INTEGER, genre TEXT
# 2. Создать функции:
# 1. Добавить фильм (заполнение делать с клавиатуры)
# 2. Получения данных обо всех фильмах
# 3. Получения данных об одном фильме по id
# 0. Выход
# 3. Функции вызывать в цикле, чтоб у пользователя был выбор.

import sqlite3

conn = sqlite3.connect('bd_sql.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, release_year INT, genre Text) ''')

# cursor.execute('''INSERT INTO movies(name,release_year,genre) VALUES ('Престиж','2006','триллер')''')
# conn.commit()
# cursor.execute('''SELECT * FROM movies''')
# k = cursor.fetchall()
# print(k)

def add_movie():
    new_name = input('Введите название нового фильмма : ')
    new_release_year = input('Введите год выхода нового фильмма : ')
    new_genre = input('Введите жанр нового фильмма : ')
    cursor.execute('''INSERT INTO movies(name,release_year,genre) VALUES (?,?,?)''', (new_name, new_release_year, new_genre))
    conn.commit()
    print("\033[4m\033[37m\033[32m{}\033[0m".format('New movie added.'))


def info_all_movie():
    cursor.execute('''SELECT * FROM movies''')
    k = cursor.fetchall()
    for i in k:
        c = ','.join([str(x) for x in i])
        print("\033[4m\033[37m\033[32m{}\033[0m".format(c))

def info_movie_id():
    id_movie = input('Введите id фильма : ')
    cursor.execute('''SELECT * FROM movies WHERE movie_id =? ''', (id_movie))
    k = cursor.fetchall()
    if k == []:
        print("\033[4m\033[37m\033[31m{}\033[0m".format('Фильма с таким id нет'))
    else:
        k = ','.join([str(x) for x in k])
        print("\033[4m\033[37m\033[32m{}\033[0m".format(k))


while True:
    print('''                   Добро пожаловать в нашу библиотеку фильмов!!!
                        Сделайте правильный выбор.
                         1. Добавить фильм (заполнение делать с клавиатуры)
                         2. Получения данных обо всех фильмах
                         3. Получения данных об одном фильме по id
                         0. Выход''')
    choise = int(input('Введите действие : '))
    if choise == 1:
        add_movie()
    elif choise == 2:
        info_all_movie()
    elif choise == 3:
        info_movie_id()
    elif choise == 0:
        print('Надеемся,что мы были полезны вам. Заходите еще.')
        break



