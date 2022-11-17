from calendar import monthrange
from datetime import datetime

dt = datetime.strptime(input(), '%Y %B')

print(monthrange(dt.year, dt.month)[1])
