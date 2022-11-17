import csv
from collections import Counter


with open('name_log.csv') as cf_in:
    _, *reader = csv.reader(cf_in)

d_num_of_changes = Counter(i[1] for i in reader)
print(*[f'{k}: {v}' for k, v in sorted(d_num_of_changes.items())], sep='\n')
