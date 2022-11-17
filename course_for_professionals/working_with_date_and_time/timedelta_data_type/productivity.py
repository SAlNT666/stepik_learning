from datetime import datetime, timedelta


date_format = '%d.%m.%Y'

start_date = datetime.strptime('20.12.2021', date_format)

print(start_date.strftime(date_format))
for x in range(1, 10):
    start_date += timedelta(days=x+1)
    print(start_date.strftime(date_format))

# print(*[(start_date + timedelta(days=sum(i for i in range(x + 1)) + x)).strftime(date_format)
#         for x in range(10)], sep='\n')
