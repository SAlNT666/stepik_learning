def get_min_max(data):
    if data:
        return data.index(min(data)), data.index(max(data))


data = [2, 3, 8, 1, 7]

print(get_min_max(data))
