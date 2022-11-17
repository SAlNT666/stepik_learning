import re

p
print(re.sub(r'(\d+)\((\w+)\)', eval(r'\1*\2'), input()))
