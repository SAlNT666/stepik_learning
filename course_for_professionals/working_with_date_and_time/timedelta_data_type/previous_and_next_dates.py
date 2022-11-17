import datetime

date_format = '%d.%m.%Y'

date = datetime.datetime.strptime(input(), date_format)

print((date - datetime.timedelta(days=1)).strftime(date_format))
print((date + datetime.timedelta(days=1)).strftime(date_format))
