# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

many_users = [
    (3, 'Peter', 'Griffin', 'male'),
    (4, 'Meg', 'Griffin', 'female'),
    (5, 'Stew', 'Griffin', 'male')
             ]

cursor.executemany("""INSERT INTO users VALUES(?, ?, ?, ?)""",
                   many_users)

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
