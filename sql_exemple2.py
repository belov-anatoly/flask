# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
orderid INT PRIMARY KEY,
date TEXT,
userid INT,
total INT);
""")

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
