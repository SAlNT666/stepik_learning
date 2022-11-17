from calendar import isleap
from datetime import date


def get_all_mondays(year):
    start = date(year, 1, 1).toordinal()
    for i in range(7):
        if date.fromordinal(start + i).weekday() == 0:
            return [date.fromordinal(j) for j in range(start + i, start + (365 + isleap(year)), 7)]
