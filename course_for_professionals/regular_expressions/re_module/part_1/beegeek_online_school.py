import re
import sys


reg_exp = r'_\d+[A-Za-z]*_?'
rows = [r.rstrip() for r in sys.stdin]

for login in (r.rstrip() for r in sys.stdin):
    print(bool(re.fullmatch(reg_exp, login)))
