def power(degree):
    return lambda x: x ** degree


square = power(2)
print(square(5))
