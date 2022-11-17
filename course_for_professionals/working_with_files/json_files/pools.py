import json
from datetime import time


with open('pools.json', encoding='utf8') as jf_in:
    pools = json.load(jf_in)


def check_time(t):
    t1, t2 = [time(int(i.split(':')[0])) for i in t.split('-')]

    if t1 <= time(10) and t2 >= time(12):
        return 1


filtered_pools = filter(lambda x: check_time(x['WorkingHoursSummer']['Понедельник']), pools)
best_pool = max(filtered_pools, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
print(f"{best_pool['DimensionsSummer']['Length']}x{best_pool['DimensionsSummer']['Width']}\n{best_pool['Address']}")
