import re


data = [input() for _ in range(5)]

for i, row in enumerate(data):
    search = re.search(r'(?<=Activation key: )([A-Z0-9]{5}[-]){4}[A-Z0-9]{5}', row)
    if search:
        print(search.group(0))
        break
