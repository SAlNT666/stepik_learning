from calendar import month_name


try:
    print(dict(enumerate(month_name[1:], 1))[int(input())])
except ValueError:
    print('Введено некорректное значение')
except KeyError:
    print('Введено число из недопустимого диапазона')
