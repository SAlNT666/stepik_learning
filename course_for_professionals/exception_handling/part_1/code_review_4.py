def get_max_index(numbers):
    max_index = 0
    max_value = numbers[-1]

    for index, value in enumerate(numbers):
        if value >= max_value:
            max_index = index
            max_value = value

    return max_index


print(get_max_index([1, 10, 2, 3]))
