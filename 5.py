# csv - comma separated values
import csv

data = [{
    'lastname': 'Кузнецов',
    'firstname': 'Пётр',
    'class_number': 9,
    'class_letter': 'A'
}, {
    'lastname': 'Меньшов',
    'firstname': 'Алексей',
    'class_number': 9,
    'class_letter': 'Б'
}]

with open('form.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for item in reader:
        for k, v in item.items():
            print(k, v)
