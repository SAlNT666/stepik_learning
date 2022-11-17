from calendar import prmonth
from datetime import datetime

dt = datetime.strptime(input(), '%Y %b')

prmonth(dt.year, dt.month)
