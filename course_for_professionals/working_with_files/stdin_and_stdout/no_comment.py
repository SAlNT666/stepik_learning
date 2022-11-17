from sys import stdin, stdout


for row in stdin:
    if not row.lstrip().startswith('#'):
        stdout.write(row)
