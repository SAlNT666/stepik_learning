import re


for link in re.findall(r'(?<=<a).*(href=")(.+)"', input()):
    print(link)
