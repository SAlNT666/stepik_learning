import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        value = func(*args, **kwargs)

        return value
    return wrapper
