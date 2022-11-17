from itertools import cycle as Cycle

# from itertools import count
#
#
# class Cycle:
#     def __new__(cls, iterable):
#         return iter(i for _ in count() for i in iterable)


cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
