from datetime import datetime, timedelta


time_format = '%H:%M:%S'

print((datetime.strptime(input(), time_format) + timedelta(seconds=int(input()))).strftime(time_format))
