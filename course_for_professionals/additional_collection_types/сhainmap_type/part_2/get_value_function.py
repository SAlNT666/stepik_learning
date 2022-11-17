from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if from_left:
        return chainmap.get(key, None)
    else:
        res = [d[key] for d in reversed(chainmap.maps) if key in d]
        return res[0] if res else None


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    return chainmap.get(key, None) if from_left else chainmap.maps[-1].get(key, None)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'}, {'age': 21})

print(get_value(chainmap, 'name', True))
