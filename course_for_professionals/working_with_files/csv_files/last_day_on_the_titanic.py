import csv


male_passengers = list()
female_passengers = list()

with open('titanic.csv', encoding='utf-8') as file_in:
    for row in csv.DictReader(file_in, delimiter=';'):
        if row['survived'] == '1' and float(row['age']) < 18:
            if row['sex'] == 'male':
                male_passengers.append(row['name'])
            elif row['sex'] == 'female':
                female_passengers.append(row['name'])

print(*male_passengers, *female_passengers, sep='\n')
