def index_of_nearest(numbers, number):
    return -1 if not numbers else numbers.index(min(numbers, key=lambda x: abs(number - x)))


print(index_of_nearest([9, 5, 3, 2, 11], 4))
