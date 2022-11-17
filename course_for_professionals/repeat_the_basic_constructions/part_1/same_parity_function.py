def same_parity(numbers):
    if not numbers:
        return []
    c = abs(numbers[0] % 2)
    return [i for i in numbers if i % 2 == c]


print(same_parity([6, 0, 67, -7, 10, -20]))
