from datetime import date, datetime


def is_available_date(booked_dates, date_for_booking):
    def get_dates_set(dates):
        dates_set = set()
        for d in dates:
            if '-' in d:
                a, b = d.split('-')
                dates_set.update({date.fromordinal(s).strftime('%d.%m.%Y') for s in
                                  range(date.toordinal(datetime.strptime(a, '%d.%m.%Y')),
                                        date.toordinal(datetime.strptime(b, '%d.%m.%Y')) + 1)})
            else:
                dates_set.add(d)
        return dates_set

    return not bool(get_dates_set(booked_dates).intersection(get_dates_set([date_for_booking])))


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

from datetime import date, time, datetime
def is_available_date(booked_dates, date_for_booking):
    ord_booked_dates = []
    for d in booked_dates:
        dates = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in d.split('-')]
        ord_booked_dates.extend(range(dates[0], dates[-1] + 1))
    dt = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in date_for_booking.split('-')]
    date_f_b = range(dt[0], dt[-1] + 1)
    return(all([i not in ord_booked_dates for i in date_f_b]))

import measure_time

is_available_date = measure_time.func_timer(is_available_date)
is_available_date(dates, some_date)
