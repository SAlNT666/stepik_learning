from re import findall

print(*findall(r'(?:7-\d{3}-\d{3}-\d{2}-\d{2})|(?:8-\d{3}-\d{4}-\d{4})', input()), sep='\n')
