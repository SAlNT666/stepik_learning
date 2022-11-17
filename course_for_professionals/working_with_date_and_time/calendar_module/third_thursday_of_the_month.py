from calendar import isleap, THURSDAY
from datetime import date


year = int(input())
start = date(year, 1, 15).toordinal()
for i in range(7):
    if date.fromordinal(start + i).weekday() == THURSDAY:
        thursdays = [date.fromordinal(j).strftime('%d.%m.%Y') for j in
                     range(start + i, start + (365 + isleap(year)), 7)
                     if 14 < date.fromordinal(j).day < 22]
        print(*thursdays, sep='\n')
        break
