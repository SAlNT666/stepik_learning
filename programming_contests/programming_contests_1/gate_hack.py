def get_extra(a, b):
    set_a = set(a)
    for i in set_a:
        if a.count(i) != b.count(i):
            return i
    return str(*set(b) - set_a)


print(get_extra(input(), input()))
