from sys import stdin
from datetime import datetime


dates = [datetime.strptime(dt.rstrip(), '%d.%m.%Y') for dt in stdin]
sorted_dates = sorted(set(dates))
r_sorted_dates = sorted_dates[::-1]

if dates == sorted_dates:
    print('ASC')
elif dates == r_sorted_dates:
    print('DESC')
else:
    print('MIX')
