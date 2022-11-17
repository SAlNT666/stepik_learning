def flatten(nested_list):
    for i in nested_list:
        yield from flatten(i) if isinstance(i, list) else [i]


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
