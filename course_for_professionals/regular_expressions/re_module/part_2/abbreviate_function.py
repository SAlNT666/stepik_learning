abbreviate = lambda phrase: ''.join(w[0].upper() + ''.join(l for l in w[1:] if l.isupper()) for w in phrase.split())

print(abbreviate('javaScript object notation'))
# print(''.join(l for l in input().split() if l.isupper()))
