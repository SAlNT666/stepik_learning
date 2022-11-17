data = '4 4 4 10 13'


def get_combination(cards):
    cards = sorted(int(i) for i in cards.split())
    cards_set_len, x = len(set(cards)), cards.count(cards[2])

    if cards_set_len == 1:
        return 'Шулер'

    elif cards_set_len == 5:
        if cards[4] - cards[0] == 4:
            return 'Стрит'
        else:
            return 'Старшая карта'

    elif x == 4:
        return 'Каре'

    elif cards_set_len == 2:
        return 'Фулл Хаус'

    elif cards_set_len == 4:
        return 'Пара'

    elif x == 3:
        return 'Сет'

    else:
        return 'Две пары'


print(get_combination(data))



