import csv
from datetime import datetime


names = dict()
fmt = '%d/%m/%Y %H:%M'

with open('name_log.csv', encoding='utf-8') as file_in:
    for row in csv.DictReader(file_in):
        if names.get(row['email'], 0):
            if names[row['email']][1] < datetime.strptime(row['dtime'], fmt):
                names[row['email']] = (row['username'], datetime.strptime(row['dtime'], fmt))
        else:
            names[row['email']] = (row['username'], datetime.strptime(row['dtime'], fmt))

with open('new_name_log.csv', 'w', newline='', encoding='utf-8') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(('username', 'email', 'dtime'))
    for k, v in sorted(names.items()):
        writer.writerow((v[0], k, datetime.strftime(v[1], fmt)))
