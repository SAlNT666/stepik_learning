from datetime import datetime


def num_of_sundays(year):
    return datetime(year, 12, 31).strftime('%U')


num_of_sundays(2021)
