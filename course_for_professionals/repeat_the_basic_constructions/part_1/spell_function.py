def spell(*words):
    words_dict = dict()
    for w in words:
        if len(w) > words_dict.get(w[0].lower(), 0):
            words_dict[w[0].lower()] = len(w)
    return words_dict
