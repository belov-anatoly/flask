# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

many_orders = [
    (1, '12.01.2022', 1, 3000),
    (2, '22.03.2022', 2, 2500),
    (3, '17.08.2022', 3, 2850)
             ]

cursor.executemany("""INSERT INTO orders VALUES(?, ?, ?, ?)""",
                   many_orders)

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
