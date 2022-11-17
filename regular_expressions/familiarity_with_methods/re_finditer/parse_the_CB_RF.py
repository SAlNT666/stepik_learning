import re


for money in re.finditer(r'\b\d+(?:,\d+)? ?₽', input()):
    print(money.group(0))
