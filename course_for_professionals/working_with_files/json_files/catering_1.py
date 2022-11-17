import json
from collections import defaultdict


with open('food_services.json', encoding='utf8') as jf_in:
    services = json.load(jf_in)

areas_dict, nets_dict = defaultdict(int), defaultdict(int)
for s in services:
    areas_dict[s['District']] += 1
    if s['OperatingCompany']: nets_dict[s['OperatingCompany']] += 1

print(*max(areas_dict.items(), key=lambda x: x[1]), sep=': ')
print(*max(nets_dict.items(), key=lambda x: x[1]), sep=': ')
