def get_repetition(s):
    len_s = len(s)
    res = 1
    for i in range(1, len_s // 2 + 1):
        if len_s % i == 0:
            if len(s.replace(s[:i], '')) == 0:
                res = s.count(s[:i])
                break

    return res


print(get_repetition('abobaboaaabobaboaa'))
