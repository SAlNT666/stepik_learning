def new_print(print):
    def wrapper(*args, sep=' ', end='\n'):
        print(*[i.upper() if isinstance(i, str) else i for i in args], sep=sep.upper(), end=end.upper())
    return wrapper


print = new_print(print)
