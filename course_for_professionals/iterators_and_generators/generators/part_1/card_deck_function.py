from itertools import count


def card_deck(suit):
    card_values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
    suits = ['пик', 'треф', 'бубен', 'червей']
    suits.remove(suit)
    yield from (i + ' ' + j for _ in count() for j in suits for i in card_values)


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
