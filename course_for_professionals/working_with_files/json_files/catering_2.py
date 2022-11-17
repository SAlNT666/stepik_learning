import json


with open('food_services.json', encoding='utf8') as jf_in:
    services = json.load(jf_in)

caterings = dict()
for s in services:
    if int(s['SeatsCount']) > caterings.get(s['TypeObject'], (0, 0))[1]:
        caterings[s['TypeObject']] = (s['Name'], int(s['SeatsCount']))

print(*sorted(f'{k}: {v[0]}, {v[1]}' for k, v in caterings.items()), sep='\n')
