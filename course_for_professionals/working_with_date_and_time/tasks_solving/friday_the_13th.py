from datetime import date


weekdays = [0] * 7
for i in range(1, 10_000):
    for j in range(1, 13):
        weekdays[date(i, j, 13).weekday()] += 1

print(*weekdays, sep='\n')
