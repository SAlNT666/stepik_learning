import functools


def prefix(string_, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return string_ * (not to_the_end) + func(*args, **kwargs) + string_ * to_the_end
        return wrapper
    return decorator


@prefix('€')
def get_bonus():
    return '2000'


print(get_bonus())
