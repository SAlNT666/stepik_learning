from datetime import datetime, date


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']


def fill_up_missing_dates(dates):
    date_format = '%d.%m.%Y'
    dates = [datetime.strptime(dt, date_format) for dt in dates]
    min_dt, max_dt = min(dates).toordinal(), max(dates).toordinal()
    return [date.fromordinal(odt).strftime(date_format) for odt in range(min_dt, max_dt + 1)]


fill_up_missing_dates(dates)
