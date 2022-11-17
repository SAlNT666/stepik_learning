import re
import sys


reg_exp = r'<a.*href=\"(.+)\">(.+)</a>'

[print(*x, sep=', ') for x in re.findall(reg_exp, sys.stdin.read(), re.M)]
