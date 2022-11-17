import re


data = [input() for _ in range(5)]

for i, row in enumerate(data):
    search = re.search(r'[Tt]oken|[Тт]окен', row)
    if search:
        print(i+1, search.start(), search.end())
        break
