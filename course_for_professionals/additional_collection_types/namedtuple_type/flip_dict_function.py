from collections import defaultdict


def flip_dict(dict_of_lists):
    reversed_dict = defaultdict(list)
    [reversed_dict[j].append(i) for i in dict_of_lists for j in dict_of_lists[i]]
    return reversed_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
