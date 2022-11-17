def dict_travel(nested_dicts, path=[]):
    for k, v in sorted(nested_dicts.items()):
        if not isinstance(v, dict):
            print('.'.join(path + [k]) + ':', v)
        else:
            dict_travel(v, path + [k])


data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)
