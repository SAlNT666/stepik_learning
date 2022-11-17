import re


for number in re.findall(r'https://imgur.com/[0-9A-Za-z]{7}', input()):
    print(number)
