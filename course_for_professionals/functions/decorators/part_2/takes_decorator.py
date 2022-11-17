import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, types) for arg in args + tuple(kwargs.values())):
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))
