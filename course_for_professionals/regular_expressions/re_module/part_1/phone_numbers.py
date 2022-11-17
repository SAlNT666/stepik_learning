import re
import sys


reg_exp = r'(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})'

for n in (r.rstrip() for r in sys.stdin):
    match = re.fullmatch(reg_exp, n)
    number = match.groupdict()
    print(f"Код страны: {number['country']}, Код города: {number['city']}, Номер: {number['number']}")
