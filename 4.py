# csv - comma separated values
import csv

# товар цена
goods = [('Ковёр', 5000), ('Утюг', 3500), ('Пенал', 120)]

# with open('sq.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y, z = i
#         print(x, y, z)


with open('sq.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    for i in goods:
        writer.writerow(i)
        print(i)
