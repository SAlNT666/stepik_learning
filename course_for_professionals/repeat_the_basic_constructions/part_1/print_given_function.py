def print_given(*args, **kwargs):
    for p in args:
        print(p, type(p))
    for k, v in sorted(kwargs.items()):
        print(k, v, type(v))


print_given(1, [1, 2, 3], 'three', two=2)
