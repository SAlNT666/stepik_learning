def get_all_values(nested_dicts, key):
    res = set()
    for k, v in nested_dicts.items():
        if key in nested_dicts:
            res.add(nested_dicts[key])
        if isinstance(v, dict):
            res.update(get_all_values(v, key))
    return res

my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
