import re


print('t=' + re.search(r'(?<=;t=)[0-9.+]+', input()).group(0))
