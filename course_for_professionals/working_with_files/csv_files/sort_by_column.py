import csv


col_to_sort = int(input()) - 1
with open('deniro.csv', encoding='utf-8') as file:
    data = list(csv.reader(file))

if data[0][col_to_sort].isalpha():
    def sort_by_column(x):
        return x[col_to_sort]
else:
    def sort_by_column(x):
        return int(x[col_to_sort])

for row in sorted(data, key=sort_by_column):
    print(*row, sep=',')
