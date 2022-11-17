dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}


def key_difference(dict1, dict2):
    res = {}
    for key in dict1:
        if dict2.get(key):
            if dict1[key] == dict2[key]:
                res[key] = 'equal'
            else:
                res[key] = 'changed'
            del dict2[key]
        else:
            res[key] = 'deleted'

    for key in dict2:
        res[key] = 'added'

    return res


result = key_difference(dict1, dict2)

print(result)
