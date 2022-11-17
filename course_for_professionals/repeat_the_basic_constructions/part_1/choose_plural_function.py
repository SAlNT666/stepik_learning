import re


def choose_plural(amount, declensions):
    amount = str(amount)
    green_num = r'(?:\d+[0,2-9]1)|(?:[0,2-9]?1)'
    white_num = r'(?:\d+[0,2-9][234])|(?:[0,2-9]?[234])'
    if re.fullmatch(green_num, amount):
        return amount + ' ' + declensions[0]
    elif re.fullmatch(white_num, amount):
        return amount + ' ' + declensions[1]
    else:
        return amount + ' ' + declensions[2]
