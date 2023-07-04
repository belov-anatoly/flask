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
result = cursor.execute("""SELECT * FROM films
WHERE year = ?""", (2009,)).fetchall()

# fetchall() - доставляет все полученные элементы
# fetchone() - доставляет только первый элемент
# fetchmany(N) - доставляет только N элементов

print(f'Найдено {len(result)} результатов.')

# Вывод на экран
for item in result:
    print(item)

# отключаемся от БД (disconnect)
connection.close()
