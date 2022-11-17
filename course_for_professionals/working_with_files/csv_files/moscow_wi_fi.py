import csv


districts_wifi = dict()

with open('wifi.csv', encoding='utf-8') as file_in:
    file_in.readline()
    for row in csv.reader(file_in, delimiter=';'):
        districts_wifi[row[1]] = districts_wifi.get(row[1], 0) + int(row[3])

for i in sorted(districts_wifi.items(), key=lambda x: (-x[1], x[0])):
    print(f'{i[0]}: {i[1]}')
