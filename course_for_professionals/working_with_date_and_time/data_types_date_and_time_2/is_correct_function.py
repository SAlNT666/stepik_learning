import datetime


def is_correct(day, month, year):
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    return True


print(is_correct(32, 12, 2021))
