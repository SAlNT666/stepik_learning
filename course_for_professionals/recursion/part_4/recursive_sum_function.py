def recursive_sum(nested_lists):
    s = 0
    for obj in nested_lists:
        if isinstance(obj, list):
            s += recursive_sum(obj)
        else:
            s += obj
    return s


my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
