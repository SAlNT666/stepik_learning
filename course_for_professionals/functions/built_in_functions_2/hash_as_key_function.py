def hash_as_key(objects):
    temp_d = {}
    for i in objects:
        temp_d.setdefault(hash(i), []).append(i)
    return {i: j if len(j) > 1 else j[0] for i, j in temp_d.items()}


data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]

print(hash_as_key(data))
