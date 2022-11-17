import re


def is_valid(string):
    return bool(re.fullmatch(r'\d{4,6}', string))


print(is_valid('123432'))
