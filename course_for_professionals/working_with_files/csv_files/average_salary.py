import csv


with open('salary_data.csv', encoding='utf-8') as file:
    salaries = dict()
    for row in csv.DictReader(file, delimiter=';'):
        company_info = salaries.get(row['company_name'], (0, 0))
        salaries[row['company_name']] = (company_info[0] + int(row['salary']), company_info[1] + 1)

for c in sorted(salaries.items(), key=lambda x: (x[1][0] / x[1][1], x[0])):
    print(c[0])
