import re


for word in re.finditer(r'\b\w{5}\b', input()):
    print(word)
