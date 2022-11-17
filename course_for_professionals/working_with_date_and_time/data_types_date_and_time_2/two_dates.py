import datetime


date1, date2 = input(), input()
print(datetime.date.fromisoformat(min(date1, date2)).strftime('%d-%m (%Y)'))
