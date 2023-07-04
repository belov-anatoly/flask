# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся
connection = sqlite3.connect('films_db.sqlite')

# создаём курсор
cursor = connection.cursor()

# Изменение записей
# UPDATE имя таблицы
# SET название поля = значение
# WHERE условие
result = cursor.execute("""DELETE from films where year < 1985""")

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
