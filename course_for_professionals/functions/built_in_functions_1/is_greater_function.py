def is_greater(lists, number):
    return number < max(sum(i) for i in lists)


data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
