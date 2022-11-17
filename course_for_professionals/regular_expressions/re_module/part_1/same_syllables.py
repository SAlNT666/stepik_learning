import re
import sys


[print(r, end='') for r in sys.stdin if re.search(r'\b(\w+)\1\b', r)]
