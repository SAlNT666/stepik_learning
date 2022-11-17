import csv
from datetime import datetime


with open('meetings.csv', encoding='utf-8') as cf_in:
    _, *meetings = list(csv.reader(cf_in))

for m in sorted(meetings, key=lambda x: datetime.strptime(x[2] + x[3], '%d.%m.%Y%H:%M')):
    print(m[0] + ' ' + m[1])
