from calendar import monthrange, month_name
from datetime import date


def get_days_in_month(year, month):
    month = list(month_name).index(month)
    return [date(year, month, day) for day in range(1, monthrange(year, month)[1] + 1)]
