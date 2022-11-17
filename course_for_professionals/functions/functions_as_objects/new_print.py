from sys import stdout


def pprint(*args, sep=' ', end='\n'):
    stdout.write(sep.upper().join([str(x.upper()) if isinstance(x, str) else str(x) for x in args]) + end.upper())


words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
pprint('beegeek', [1, 2, 3], 4)
