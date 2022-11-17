import csv


with open('data.csv') as cf_in:
    _, *reader = csv.reader(cf_in)
    print(sum(int(r[1]) for r in reader if r[-1] == 'a'))
