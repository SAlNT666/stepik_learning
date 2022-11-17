from datetime import datetime

dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]

diffs = [abs(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]

print(diffs)
