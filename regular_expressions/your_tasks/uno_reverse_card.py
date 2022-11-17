import re


text = '123'
five_symbols = re.search('(.)?(.)?(.)?(.)?(.)?', text)
print(text[:-5] + ''.join(s for s in five_symbols.groups() if s))
