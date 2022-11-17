def add_to_list_in_dict(data, key, element):
    try:
        data[key]
    except KeyError:
        data[key] = list()
    finally:
        data[key].append(element)


data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'c', 7)

print(data)
