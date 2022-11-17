from sys import stdin


print(sum(row.lstrip().startswith('#') for row in stdin))
