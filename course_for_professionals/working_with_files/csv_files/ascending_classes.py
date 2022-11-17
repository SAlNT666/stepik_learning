import csv


def key_func(grade):
    number, letter = grade.split('-')
    return int(number), letter


with open('student_counts.csv', encoding='utf-8') as file_in:
    reader = csv.DictReader(file_in)
    columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)

with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file_out:
    writer = csv.DictWriter(file_out, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
