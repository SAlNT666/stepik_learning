def filter_anagrams(word, words):
    res = []

    def create_dict(word):
        new_dict = dict()
        for l in word:
            new_dict[l] = new_dict.get(l, 0) + 1
        return new_dict

    word_d = create_dict(word)

    for w in words:
        w_d = create_dict(w)
        if word_d == w_d: res.append(w)
    return res


print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolrert']))
