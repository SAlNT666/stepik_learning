def non_negative_even(numbers):
    return all(i % 2 == 0 and i >= 0 for i in numbers)


print(non_negative_even([0, 2, 4, 8, 16]))
