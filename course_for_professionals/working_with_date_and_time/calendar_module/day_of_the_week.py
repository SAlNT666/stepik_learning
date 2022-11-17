from calendar import weekday, day_name
from datetime import datetime


dt = datetime.strptime(input(), '%Y-%m-%d')
print(day_name[weekday(dt.year, dt.month, dt.day)])
