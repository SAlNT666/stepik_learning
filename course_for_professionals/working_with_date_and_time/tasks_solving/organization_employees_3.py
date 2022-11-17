from datetime import datetime, timedelta

fmt, data = '%d.%m.%Y', {}
dt = datetime.strptime(input(), fmt)
start = dt + timedelta(days=1)
end = dt + timedelta(days=7)

for _ in range(int(input())):
    *name, birthday = input().split()
    name, birthday = ' '.join(name), datetime.strptime(birthday, fmt)
    if start <= birthday.replace(year=start.year) <= end:
        data[birthday] = name
    elif start <= birthday.replace(year=end.year) <= end:
        data[birthday] = name

if data:
    print(data[max(data)])
else:
    print('Дни рождения не планируются')
