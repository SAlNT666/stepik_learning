import time


def calculate_it(func, *args):
    start = time.monotonic()
    res = func(*args)
    return res, time.monotonic() - start
