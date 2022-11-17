from datetime import datetime, timedelta


start = datetime.strptime(input(), '%d.%m.%Y')
end = datetime.strptime(input(), '%d.%m.%Y')


while start <= end:
    if (start.month + start.day) % 2:
        while start <= end:
            if start.weekday() not in (0, 3):
                print(start.strftime('%d.%m.%Y'))
            start += timedelta(days=3)
    start += timedelta(days=1)
