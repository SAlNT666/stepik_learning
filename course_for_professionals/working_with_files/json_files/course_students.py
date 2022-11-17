import json
import csv


with open('students.json', encoding='utf8') as jf_in:
    students = json.load(jf_in)

student_phones = dict()
with open('data.csv', 'w', newline='', encoding='utf-8') as jf_out:
    writer = csv.writer(jf_out)
    writer.writerow(('name', 'phone'))
    for s in sorted(students, key=lambda x: x['name']):
        if s['age'] > 17 and s['progress'] > 74:
            writer.writerow((s['name'], s['phone']))
