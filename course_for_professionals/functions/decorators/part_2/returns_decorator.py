import functools


def returns(type_):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(result := func(*args, **kwargs), type_):
                return result
            else:
                raise TypeError
        return wrapper
    return decorator


@returns(int)
def add(a, b):
    return a + b

print(add(10, 5))
