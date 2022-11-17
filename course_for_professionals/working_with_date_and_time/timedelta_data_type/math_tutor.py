from datetime import datetime, timedelta


time_format = '%H:%M'

start, end = datetime.strptime(input(), time_format), datetime.strptime(input(), time_format)

end -= timedelta(minutes=45)
while start <= end:
    print(start.strftime(time_format), '-', (start + timedelta(minutes=45)).strftime(time_format))
    start += timedelta(minutes=55)
