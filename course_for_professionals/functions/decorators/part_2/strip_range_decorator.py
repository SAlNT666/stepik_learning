import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result[:start] + char * (min(end, len(result)) - start) + result[end:]
        return wrapper
    return decorator


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())
