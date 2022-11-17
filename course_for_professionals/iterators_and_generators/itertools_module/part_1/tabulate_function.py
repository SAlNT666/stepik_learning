from itertools import count


tabulate = lambda func: (func(i) for i in count(1))


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))
