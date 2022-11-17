def filter_names(names, ignor_char, max_names):
    for i, name in enumerate(x for i, x in enumerate(names) if (x[0].upper() != ignor_char and x.isalpha())):
        if i >= max_names: return
        else: yield name


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
