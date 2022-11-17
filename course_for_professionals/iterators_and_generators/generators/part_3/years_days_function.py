from datetime import date, timedelta
from calendar import isleap


years_days = lambda y: (date(y, 1, 1) + timedelta(days=i) for i in range(365 + isleap(y)))


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
