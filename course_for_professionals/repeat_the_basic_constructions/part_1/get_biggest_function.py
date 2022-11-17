def get_biggest(numbers):
    if numbers:
        numbers = list(map(str, numbers))
        max_num_length = len(max(numbers, key=len))
        return int(''.join(sorted(numbers, key=lambda x: x * max_num_length, reverse=True)))
    else:
        return -1


print(get_biggest([93, 9399, 9390]))
