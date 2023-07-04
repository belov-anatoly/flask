# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
userid INT PRIMARY KEY,
fname TEXT,
lname TEXT,
gender TEXT);
""")

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
