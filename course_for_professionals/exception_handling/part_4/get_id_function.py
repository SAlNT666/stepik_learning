from re import fullmatch


def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not fullmatch(r'[A-Z][a-z]+', name):
        raise ValueError('Имя не является корректным')
    else:
        return len(names) + 1
