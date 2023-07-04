# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся
connection = sqlite3.connect('films_db.sqlite')

# создаём курсор
cursor = connection.cursor()

# запрос по "доставке" (fetch) информации
result = cursor.execute("""INSERT INTO genres 
VALUES(44, 'Байки'), (45, 'Басни')""")


connection.commit()
# отключаемся от БД (disconnect)
connection.close()
