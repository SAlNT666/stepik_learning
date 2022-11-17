import re


data = [input() for _ in range(4)]

for i, row in enumerate(data):
    search = re.search(r'[Кк]од', row)
    if search:
        print(i+1, search.start())
        break
