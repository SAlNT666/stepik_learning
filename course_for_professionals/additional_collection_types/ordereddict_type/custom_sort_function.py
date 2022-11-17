from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    [ordered_dict.move_to_end(k) for k, v in sorted(ordered_dict.items(), key=lambda x: x[by_values])]


data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items())
