from datetime import datetime, time


weekday = (time(hour=9), time(hour=21))
weekend = (time(hour=10), time(hour=18))
schedule = {0: weekday, 1: weekday,
            2: weekday, 3: weekday,
            4: weekday, 5: weekend,
            6: weekend}

dt = datetime.strptime('05.11.2021 21:00', '%d.%m.%Y %H:%M')
schedule_day = schedule[dt.weekday()]
dt = dt.time()
if schedule_day[0] > dt or schedule_day[1] <= dt:
    print('Магазин не работает')
else:
    print((schedule_day[1].hour - dt.hour) * 60 + schedule_day[1].minute - dt.minute)

