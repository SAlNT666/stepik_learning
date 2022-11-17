import string


results = ('ru', 'mix', 'mix', 'en')
print(string.ascii_letters[sum(input() in string.ascii_letters for _ in range(3))])
