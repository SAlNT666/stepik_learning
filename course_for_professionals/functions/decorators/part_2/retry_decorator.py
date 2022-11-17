import functools


class MaxRetriesException(Exception):
    ...


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    ...
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))
