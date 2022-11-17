import csv


with open('sales.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        if int(row['old_price']) > int(row['new_price']):
            print(row['name'])
