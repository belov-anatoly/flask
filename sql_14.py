# PEP-8 (Python Enhancement Proposal)
# PEP-249 (Python Database API Specification)
# Подключение (Connection) - объект
# Курсор - объект для работы внутри БД
import sqlite3

# подключаемся или создаём
connection = sqlite3.connect('shop.sqlite')

# создаём курсор
cursor = connection.cursor()

# many_orders = [
#     (4, '22.05.2022', 4, 3200),
#     (5, '02.04.2022', 2, 1500),
#     (6, '27.09.2022', 3, 1850)
#              ]
maxid = cursor.execute("""SELECT MAX(userid) from users""").fetchone()
num = maxid[0] + 1
cursor.execute(f"""INSERT INTO users (userid, fname, lname, gender)
VALUES({num}, 'John', 'Lord', 'male')""")

# Подтверждение действия
connection.commit()
# отключаемся от БД (disconnect)
connection.close()
