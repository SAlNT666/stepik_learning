def hide_card(card_number):
    return '*' * 12 + card_number.replace(' ', '')[-4:]


card = '1234567890123456'
print(hide_card(card))
