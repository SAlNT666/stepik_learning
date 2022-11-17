def polynom(x):
    value = x**2 + 1
    if 'values' not in polynom.__dict__:
        polynom.values = set()
    polynom.values.add(value)
    return value

print(polynom(5))
print(polynom.values)
