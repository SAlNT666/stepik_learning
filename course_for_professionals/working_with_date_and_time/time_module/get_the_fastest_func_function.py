import time


def get_the_fastest_func(funcs, arg):
    best_time = 999
    fastet_func = ''
    for func in funcs:
        start = time.monotonic()
        func(arg)
        time_res = time.monotonic() - start
        if time_res < best_time:
            best_time = time_res
            fastest_func = func
    return fastest_func


