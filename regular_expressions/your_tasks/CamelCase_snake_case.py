import re


def camel_to_snake(str):
    s1 = re.sub('(.)([A-Z\d]+)', r'\1_\2', str)
    return re.sub('([a-z\d])([A-Z])', r'\1_\2', s1).lower()


print(camel_to_snake(input()))
