import json
from collections import defaultdict


with open('countries.json', encoding='utf8') as jf_in:
    countries = json.load(jf_in)

religions = defaultdict(list)

for c in countries:
    religions[c['religion']].append(c['country'])

with open('religion.json', 'w', encoding='utf8') as jf_out:
    json.dump(religions, jf_out)
