from datetime import date, timedelta


def dates(start, count=None):
    count = count or (date.max - start).days + 1
    yield from (start + timedelta(days=i) for i in range(count))


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))
