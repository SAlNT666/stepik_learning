import csv
import json


sports_grounds = dict()
with open('playgrounds.csv', encoding='utf8') as jf_in:
    reader = csv.DictReader(jf_in, delimiter=';')
    for row in reader:
        sports_grounds.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])


with open('addresses.json', 'w', encoding='utf8') as f_out:
    json.dump(sports_grounds, f_out, ensure_ascii=False, indent=3)
