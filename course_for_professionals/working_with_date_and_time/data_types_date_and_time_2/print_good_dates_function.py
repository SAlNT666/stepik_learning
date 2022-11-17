from datetime import date


def print_good_dates(dates):
    print(*[x.strftime('%B %d, %Y') for x in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates))],
          sep='\n')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
