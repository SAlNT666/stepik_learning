import csv


with open('prices.csv', encoding='utf-8') as file_in:
    headers, *rows = csv.reader(file_in, delimiter=';')

min_price = min([(int(r[i]), headers[i], r[0]) for i in range(1, len(headers)) for r in rows])
print(f'{min_price[1]}: {min_price[2]}')
