def takes_positive(func):
    def wrapper(*args, **kwargs):
        for i in args + tuple(kwargs.values()):
            if not isinstance(i, int):
                raise TypeError
            elif i < 1:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))
