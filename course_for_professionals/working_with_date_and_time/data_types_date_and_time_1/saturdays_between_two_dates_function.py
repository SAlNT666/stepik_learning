from datetime import date


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start

    return sum(1 for i in range(start.toordinal(), end.toordinal() + 1)
               if date.weekday(date.fromordinal(i)) == 5)


date1 = date(1998, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))
