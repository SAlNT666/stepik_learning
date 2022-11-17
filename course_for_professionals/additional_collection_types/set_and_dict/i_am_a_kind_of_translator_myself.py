from string import ascii_lowercase


alphabet = input()
txt = input().lower()

tbl = txt.maketrans(ascii_lowercase, alphabet)

print(txt.translate(tbl))
