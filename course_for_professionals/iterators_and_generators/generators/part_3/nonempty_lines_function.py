def nonempty_lines(file):
    with open(file, encoding='utf-8') as f_in:
        yield from (('...', l.rstrip('\n'))[len(l) < 25] for l in f_in if l.rstrip('\n'))


print(*nonempty_lines('data.txt'))
