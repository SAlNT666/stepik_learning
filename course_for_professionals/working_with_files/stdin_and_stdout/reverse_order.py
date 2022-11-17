import sys

for row in sys.stdin:
    print(row.strip()[::-1])
