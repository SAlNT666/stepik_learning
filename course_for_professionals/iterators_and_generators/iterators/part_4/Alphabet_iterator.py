from string import ascii_lowercase
from itertools import cycle


class Alphabet:
    def __new__(cls, language):
        l_dict = {'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 'en': ascii_lowercase}
        return cycle(l_dict[language])


ru_alpha = Alphabet('ru')

for _ in range(1000):
    next(ru_alpha)

print(next(ru_alpha))
