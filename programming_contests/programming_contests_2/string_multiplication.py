from re import subn

rex = r'(\d+)\((\w+)\)'
text = 'bbbb10(2(a))bb3(b)'
print(text)
number_of_substitutions = 1

while number_of_substitutions:
    text, number_of_substitutions = subn(rex, lambda s: int(s.group(1)) * s.group(2), text)

print(text)
