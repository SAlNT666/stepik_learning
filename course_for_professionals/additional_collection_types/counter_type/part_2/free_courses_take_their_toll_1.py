import csv
import json
from collections import Counter


weights = Counter()
n_cf_in = 4
for n in range(1, n_cf_in+1):
    with open(f'quarter{n}.csv', encoding='utf-8') as cf_in:
        _, *rows = csv.reader(cf_in)
    weights += Counter({r[0]: sum(int(i) for i in r[1:]) for r in rows})

with open('prices.json', encoding='utf-8') as jf_in:
    prices = json.load(jf_in)

print(sum(weights[i] * prices[i] for i in weights))
