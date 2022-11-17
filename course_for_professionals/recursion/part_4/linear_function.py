from functools import reduce


def linear(nested_lists):
    if isinstance(nested_lists, int):
        return [nested_lists]
    else:
        return reduce(lambda x, y: x + linear(y), nested_lists, [])


my_list = [[1, 2], [4, 4], 2, [1, [2, 10]]]

print(linear(my_list))
