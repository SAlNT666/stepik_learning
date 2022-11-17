import re


def snake_to_camel(str):
    s1 = re.sub(r'(^|[_])(\w)', lambda x: x[2].upper(), str)
    return s1


print(snake_to_camel(input()))
