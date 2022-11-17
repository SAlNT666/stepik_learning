def generator_square_polynom(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = generator_square_polynom(1, 2, 1)
print(f(5))
