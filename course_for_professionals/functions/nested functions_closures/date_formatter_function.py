from datetime import date


def date_formatter(country_code):
    d_frmt = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
              'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}[country_code]

    return lambda d: date.strftime(d, d_frmt)



date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
