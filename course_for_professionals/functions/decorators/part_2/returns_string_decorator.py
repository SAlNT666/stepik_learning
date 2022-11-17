import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if isinstance(result := func(*args, **kwargs), str):
            return result
        else:
            raise TypeError
    return wrapper


@returns_string
def beegeek():
    return 'beegeek'


print(beegeek())
