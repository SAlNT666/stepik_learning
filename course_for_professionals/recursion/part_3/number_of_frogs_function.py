def number_of_frogs(year):
    return 77 if year == 1 else 3 * (number_of_frogs(year - 1) - 30)


print(number_of_frogs(2))
