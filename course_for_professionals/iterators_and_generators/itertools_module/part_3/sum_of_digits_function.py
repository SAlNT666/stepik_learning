def sum_of_digits(iterable):
    return sum(sum(int(i) for i in str(n)) for n in iterable)


print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
