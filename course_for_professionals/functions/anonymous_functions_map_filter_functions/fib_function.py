fib_d = {1: 1, 2: 1}
fib = lambda x: fib_d[x] if x in fib_d else fib_d.setdefault(x, fib(x - 1) + fib(x-2))

print(fib(5))
