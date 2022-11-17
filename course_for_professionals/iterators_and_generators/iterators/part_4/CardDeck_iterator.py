class CardDeck:
    def __new__(cls):
        card_values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        suits = ('пик', 'треф', 'бубен', 'червей')
        return iter(i + ' ' + j for j in suits for i in card_values)


cards = CardDeck()
print(*cards)
