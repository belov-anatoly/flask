# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

cursor.execute("""
INSERT INTO users(userid, fname, lname, gender)
VALUES(1, 'Alex', 'Smith', 'male')
""")

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
