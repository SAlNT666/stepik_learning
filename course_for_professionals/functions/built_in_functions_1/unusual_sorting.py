print(''.join(sorted(input(), key=lambda x: (not x.isalpha(), not x.islower(), x.isdigit() and not int(x) % 2, x))))
